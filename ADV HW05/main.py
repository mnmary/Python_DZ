from pprint import pprint
import re
import csv


def normalize_fio(row):
    fio = ' '.join(row[:3]).split()[:3]
    while len(fio) < 3:
        fio.append('')
    return fio


def main():
    with open("phonebook_raw.csv", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    header = contacts_list[0]
    contacts = contacts_list[1:]

    PHONE_PATTERN = r"(\+7|8)[\s(]*(\d{3})[)\s]*[\s-]*(\d{3})[\s-]*(\d{2})[\s-]*(\d{2})[\s(]*(доб.)*\s*(\d{4})*"
    PHONE_SUB = r"+7(\2)\3-\4-\5 \6\7"

    result = {}

    for row in contacts:
        fio = normalize_fio(row)
        lastname, firstname, surname = fio
        org, position, phone, email = row[3:7]

        phone = re.sub(PHONE_PATTERN, PHONE_SUB, phone)

        key = (lastname, firstname)
        new_contact = [lastname, firstname, surname, org, position, phone, email]

        if key in result:
            for i in range(len(new_contact)):
                if result[key][i] == '':
                    result[key][i] = new_contact[i]
        else:
            result[key] = new_contact

    normalize_contacts = header + list(result.values())

    with open("phonebook.csv", "w", encoding="utf-8", newline='') as f:
        writer = csv.writer(f)
        writer.writerows(normalize_contacts)

    pprint(normalize_contacts)


if __name__ == "__main__":
    main()
