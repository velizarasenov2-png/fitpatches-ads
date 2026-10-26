// Shopify Admin GraphQL: read recent orders, remember which messages were sent (order metafield fitpatches.msgs).
export const NAMESPACE = 'fitpatches';

export const ORDERS_QUERY = `query RecentOrders($q: String!, $after: String) {
  orders(first: 20, after: $after, query: $q, sortKey: CREATED_AT, reverse: true) {
    pageInfo { hasNextPage endCursor }
    nodes {
      id
      name
      createdAt
      cancelledAt
      displayFinancialStatus
      tags
      phone
      shippingAddress { firstName phone address1 city }
      customer { firstName }
      shippingLine { title }
      totalOutstandingSet { presentmentMoney { amount currencyCode } }
      fulfillments(first: 2) {
        createdAt
        displayStatus
        trackingInfo(first: 1) { company number url }
        events(first: 15, sortKey: HAPPENED_AT) { nodes { status happenedAt } }
      }
      msgs: metafield(namespace: "fitpatches", key: "msgs") { value }
      msgsTest: metafield(namespace: "fitpatches", key: "msgs_test") { value }
    }
  }
}`;

export const SAVE_MUTATION = `mutation SaveSent($metafields: [MetafieldsSetInput!]!) {
  metafieldsSet(metafields: $metafields) {
    metafields { key }
    userErrors { field message code }
  }
}`;

export async function createShopify(cfg, fetchImpl = fetch) {
  let token = cfg.shopifyAccessToken;
  if (!token) {
    const res = await fetchImpl(`https://${cfg.shopifyShop}/admin/oauth/access_token`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
      body: new URLSearchParams({
        grant_type: 'client_credentials',
        client_id: cfg.shopifyClientId,
        client_secret: cfg.shopifyClientSecret,
      }),
    });
    if (!res.ok) throw new Error(`Shopify не даде токен (HTTP ${res.status}). Проверете Client ID/Secret и дали приложението е инсталирано.`);
    token = (await res.json()).access_token;
  }

  async function gql(query, variables) {
    const res = await fetchImpl(`https://${cfg.shopifyShop}/admin/api/${cfg.shopifyApiVersion}/graphql.json`, {
      method: 'POST',
      headers: { 'Content-Type': 'application/json', 'X-Shopify-Access-Token': token },
      body: JSON.stringify({ query, variables }),
    });
    const json = await res.json().catch(() => null);
    if (!res.ok || !json || json.errors) {
      throw new Error(`Shopify GraphQL HTTP ${res.status}: ${JSON.stringify(json?.errors ?? null).slice(0, 300)}`);
    }
    return json.data;
  }

  return {
    async recentOrders(since) {
      const q = `created_at:>=${since.toISOString().slice(0, 10)}`;
      const out = [];
      let after = null;
      for (let page = 0; page < 30; page++) {
        const data = await gql(ORDERS_QUERY, { q, after });
        out.push(...data.orders.nodes);
        if (!data.orders.pageInfo.hasNextPage) break;
        after = data.orders.pageInfo.endCursor;
      }
      return out;
    },

    async saveSent(orderId, key, sent) {
      const data = await gql(SAVE_MUTATION, {
        metafields: [{ ownerId: orderId, namespace: NAMESPACE, key, type: 'json', value: JSON.stringify(sent) }],
      });
      const errs = data.metafieldsSet.userErrors;
      if (errs.length) throw new Error(`Shopify metafieldsSet: ${errs.map((e) => e.message).join('; ')}`);
    },
  };
}
