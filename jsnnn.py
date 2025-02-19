import json

# Открываем JSON-файл
with open('sample-data.json') as file:
    data = json.load(file)

# Заголовок таблицы
print("Interface Status")
print("=" * 80)
print("DN".ljust(50) + "Description".ljust(20) + "Speed".ljust(8) + "MTU")
print("-" * 50 + " " + "-" * 20 + " " + "-" * 6 + " " + "-" * 4)

# Проходим по каждому интерфейсу
for item in data["imdata"]:
    attributes = item["l1PhysIf"]["attributes"]
    dn = attributes.get("dn", "").ljust(50)
    descr = attributes.get("descr", "").ljust(20)
    speed = attributes.get("speed", "inherit").ljust(8)
    mtu = attributes.get("mtu", "9150")
    print(dn + descr + speed + mtu)
в