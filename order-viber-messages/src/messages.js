// Message texts. Viber gets the full Cyrillic text; the SMS fallback is short Latin text so it fits in one SMS.
const PRODUCT = 'розовите лепенки FitPatches за намаляване на апетита';
const COURIER = { econt: 'Еконт', speedy: 'Спиди' };
const COURIER_LAT = { econt: 'Econt', speedy: 'Speedy' };

const TRANSLIT = {
  а: 'a', б: 'b', в: 'v', г: 'g', д: 'd', е: 'e', ж: 'zh', з: 'z', и: 'i', й: 'y', к: 'k', л: 'l', м: 'm',
  н: 'n', о: 'o', п: 'p', р: 'r', с: 's', т: 't', у: 'u', ф: 'f', х: 'h', ц: 'ts', ч: 'ch', ш: 'sh',
  щ: 'sht', ъ: 'a', ь: 'y', ю: 'yu', я: 'ya', ё: 'yo', ы: 'i', э: 'e',
};

// Bulgarian streamlined transliteration, reduced to plain GSM-7 characters.
export function toLatin(s) {
  return String(s ?? '')
    .replace(/ия(?![а-яё])/g, 'ia')
    .replace(/ИЯ(?![А-ЯЁ])/g, 'IA')
    .replace(/[а-яё]/gi, (ch) => {
      const lat = TRANSLIT[ch.toLowerCase()];
      if (ch === ch.toLowerCase()) return lat;
      return lat.charAt(0).toUpperCase() + lat.slice(1);
    })
    .replace(/№/g, 'No')
    .replace(/[^A-Za-z0-9 .,:;!?'"()\-\/+&%#*@]/g, '')
    .replace(/\s+/g, ' ')
    .trim();
}

const money = (n) => (Math.round(n * 100) / 100).toFixed(2);

function fit(parts, max = 160) {
  let text = parts.filter(Boolean).join(' ');
  return text.length <= max ? text : text.slice(0, max - 1).trimEnd() + '.';
}

export function render(type, info, cfg) {
  const name = info.firstName;
  const hello = name ? `Здравейте, ${name}!` : 'Здравейте!';
  const helloLat = name ? `${toLatin(name)}, ` : '';
  const courier = COURIER[info.courier] || 'куриера';
  const courierLat = COURIER_LAT[info.courier] || 'kuriera';
  const office = info.office?.text || '';
  // Address orders that ended up in an office have no office address in the order.
  const atOffice = office ? `в офиса на ${courier} – ${office}` : `в офис на ${courier}`;
  const officeLat = info.office?.city ? ' ' + toLatin(info.office.city).slice(0, 25) : '';
  const tracking = info.fulfillment?.tracking || '';
  const hasAmount = info.amount > 0;
  const amount = `${money(info.amount)} ${info.currency === 'EUR' ? '€' : info.currency}`;
  const amountLat = `${money(info.amount)} ${info.currency}`;
  const phone = cfg.supportPhone;

  switch (type) {
    case 'thanks': {
      const where = info.isOffice ? `офис на ${courier} – ${office}` : `до адрес ${info.courier === 'speedy' ? 'със' : 'с'} ${courier}`;
      return {
        viber: [
          `${hello} 💗`,
          'Благодарим Ви за поръчката във FitPatches!',
          '',
          `💗 ${PRODUCT[0].toUpperCase()}${PRODUCT.slice(1)}`,
          hasAmount ? `💶 Сума при получаване: ${amount}` : null,
          `📍 Доставка: ${where}`,
          '',
          `Ще Ви пишем, когато пратката пристигне. За въпроси: ${phone}`,
        ].filter((l) => l !== null).join('\n'),
        sms: fit([
          name ? `FitPatches: Blagodarim za porachkata, ${toLatin(name)}!` : 'FitPatches: Blagodarim za porachkata!',
          `Rozovite lepenki za namalyavane na apetita idvat ${info.courier === 'speedy' ? 'sas' : 's'} ${courierLat}.`,
          hasAmount ? `Suma ${amountLat}.` : '',
          `Tel. ${phone}`,
        ]),
      };
    }
    case 'office':
      return {
        viber: [
          `${hello} 📦`,
          `Вашите розови лепенки FitPatches за намаляване на апетита вече Ви чакат в офиса на ${courier}:`,
          office ? `📍 ${office}` : null,
          `🔢 Товарителница: ${tracking}`,
          hasAmount ? `💶 Сума за плащане: ${amount}` : null,
          '',
          'Вземете я, когато Ви е удобно. Пратките се пазят в офиса само няколко дни.',
        ].filter((l) => l !== null).join('\n'),
        sms: fit([
          `FitPatches: ${helloLat}rozovite lepenki za namalyavane na apetita vi chakat v ofis ${courierLat}${officeLat}.`,
          `Tovaritelnitsa ${tracking}${hasAmount ? `, suma ${amountLat}` : ''}.`,
        ]),
      };
    case 'office_reminder':
      return {
        viber: [
          `${hello} 💗`,
          `Напомняме, че ${PRODUCT} още Ви чакат ${atOffice}.`,
          `🔢 Товарителница: ${tracking}${hasAmount ? ` · 💶 Сума: ${amount}` : ''}`,
          `Ако не можете да я вземете, обадете ни се: ${phone}`,
        ].join('\n'),
        sms: fit([
          `FitPatches: Napomnyane - lepenkite vi chakat v ofis ${courierLat}${officeLat}.`,
          `Tovaritelnitsa ${tracking}${hasAmount ? `, suma ${amountLat}` : ''}.`,
          `Tel. ${phone}`,
        ]),
      };
    case 'office_last':
      return {
        viber: [
          `${hello} ⏰`,
          `Последно напомняне: пратката Ви с ${PRODUCT} е ${atOffice}. Ако не бъде взета в следващите дни, куриерът ще я върне.`,
          `🔢 Товарителница: ${tracking}${hasAmount ? ` · 💶 Сума: ${amount}` : ''}`,
        ].join('\n'),
        sms: fit([
          `FitPatches: Posledno napomnyane - pratkata vi e v ofis ${courierLat}${officeLat} i skoro shte bade varnata.`,
          `Tovaritelnitsa ${tracking}${hasAmount ? `, suma ${amountLat}` : ''}.`,
        ]),
      };
    case 'address_out':
      return {
        viber: [
          `${hello} 🚚`,
          `Днес куриер на ${courier} ще Ви донесе ${PRODUCT}.`,
          `🔢 Товарителница: ${tracking}`,
          hasAmount ? `💶 Пригответе ${amount} за плащане.` : null,
        ].filter((l) => l !== null).join('\n'),
        sms: fit([
          `FitPatches: ${helloLat}dnes kurier na ${courierLat} shte vi donese rozovite lepenki za namalyavane na apetita.`,
          `Tovaritelnitsa ${tracking}${hasAmount ? `, prigotvete ${amountLat}` : ''}.`,
        ]),
      };
    case 'address_failed':
      return {
        viber: [
          `${hello} Куриерът на ${courier} не успя да Ви открие днес с ${PRODUCT}.`,
          `🔢 Товарителница: ${tracking}`,
          `Обадете ни се на ${phone}, за да уточним кога да Ви я донесат.`,
        ].join('\n'),
        sms: fit([
          `FitPatches: ${helloLat}kurierat na ${courierLat} ne uspya da vi otkrie dnes.`,
          `Tovaritelnitsa ${tracking}. Obadete ni se: ${phone}`,
        ]),
      };
    default:
      throw new Error(`Непознат тип съобщение: ${type}`);
  }
}
