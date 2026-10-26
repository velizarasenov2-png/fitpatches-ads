// Builds HTML in the same structure as my.bigarena.net/tracking/order/... pages (all data here is made up).
export function trackingHtml(events, { courier = 'Спиди', number = '60000000001' } = {}) {
  const head = `<div class="tracking-shipment-container">
            <div class="tracking-shipment-box tracking-shipment-box-details">
            <div class="tracking-shipment-row tracking-shipment-row-mb-1">
                <div class="tracking-shipment-col tracking-shipment-title tracking-shipment-bold">Куриер                    :
                </div>
                <div class="tracking-shipment-col tracking-shipment-title">
                                            ${courier}
                        - до офис
                                    </div>
            </div>
            </div>`;
  if (!events.length) {
    return `<html><body>${head}
                    <div class="tracking-shipment-box tracking-shipment-box-details">
                <div class="tracking-shipment-row tracking-shipment-row-mb-1 tracking-shipment-justify-content-center">
                    <div class="tracking-shipment-title tracking-shipment-bold">Няма данни за товарителницата</div>
                </div>
            </div>
            </div></body></html>`;
  }
  const blocks = events.map(([date, city, text], i) => `
                <div class="tracking-shipment-box tracking-shipment-box-steps">
                    <div class="tracking-shipment-box-steps-header">
                        <div class="tracking-shipment-box-steps-container">
                            <div class="tracking-shipment-box-steps-date">
                                ${date}${city ? `                                      - ${city}` : ''}
                                                            </div>
                        </div>
                    </div>
                    <div class="tracking-shipment-box-steps-body">
                        <div class="tracking-shipment-box-steps-container">
                            <div class="tracking-shipment-box-steps-step"><span>${i + 1}</span></div>
                            <div class="tracking-shipment-box-steps-number tracking-shipment-bold tracking-shipment-title">
                                #${number}
                            </div>
                        </div>
                        <div class="tracking-shipment-box-steps-container tracking-shipment-mb-1">
                            <div class="tracking-shipment-box-steps-line"></div>
                            <div class="tracking-shipment-box-steps-message">
                                 ${text}                            </div>
                        </div>
                    </div>
                </div>`);
  return `<html><body>${head}${blocks.join('')}
            </div></body></html>`;
}

export const baseCfg = {
  supportPhone: '0887459494',
  live: true,
  testPhone: '',
  startAt: new Date('2026-10-01T00:00:00Z'),
  sendHours: '08:00-21:00',
  lookbackDays: 14,
  thanksDelayMinutes: 5,
  reminderDays: [2, 4],
  maxSendsPerRun: 40,
  printTexts: false,
  viberSender: 'FitPatches',
  viberExpiration: 3600,
  viberTemplates: false,
  viberTemplateLanguage: 'bg',
  smsSenderId: 'gSystem',
  smsSenderValue: '',
  bulkgateAppId: '1',
  bulkgateToken: 't',
};

// A Shopify order node shaped like the ORDERS_QUERY result (made-up customer).
export function orderNode(over = {}) {
  return {
    id: 'gid://shopify/Order/1',
    name: '#2001',
    createdAt: '2026-10-26T08:00:00Z',
    cancelledAt: null,
    displayFinancialStatus: 'PENDING',
    tags: ['Middleware.bg'],
    phone: '+359888000111',
    shippingAddress: {
      firstName: 'Мария',
      phone: '+359888000111',
      address1: 'До офис econt[7538]: Айдемир -  Айдемир кв. Деленките ул. София №7',
      city: 'Айдемир',
    },
    customer: { firstName: 'Мария' },
    shippingLine: { title: 'До офис econt' },
    totalOutstandingSet: { presentmentMoney: { amount: '25.38', currencyCode: 'EUR' } },
    fulfillments: [],
    msgs: null,
    msgsTest: null,
    ...over,
  };
}

export function fulfillment(number, events = [], displayStatus = 'FULFILLED', company = 'Еконт експрес') {
  return {
    createdAt: '2026-10-26T10:00:00Z',
    displayStatus,
    trackingInfo: [{ company, number, url: '' }],
    events: { nodes: events.map(([status, happenedAt]) => ({ status, happenedAt })) },
  };
}
