import random
import mysql.connector

people = ['01', '05', '06', '09', '011', '012', '013', '015', '016', '018', '020', '021', '022', '024', '026', '027', '031', '032', 'temp1', 'temp2', 'temp3', 'temp4', 'temp5']
tester = ", "
test = []
easy = []
hard = []

for i in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '24', '25']:
    for j in range(5):
        easy.append(str(i))

for i in ['11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23']:
    for j in range(5):
        hard.append(str(i))

for i in people:
    num_test = []
    for j in range(2):
        get_easy = random.choice(easy)
        get_hard = random.choice(hard)
        while get_easy in num_test:
            get_easy = random.choice(easy)
        while get_hard in num_test:
            get_hard = random.choice(hard)
        num_test.append(get_easy)
        num_test.append(get_hard)
        easy.remove(get_easy)
        hard.remove(get_hard)
    print(f"Number {i} Test is {tester.join(num_test)}")

print()
print("-----------ข้อเหลือ-----------")
print(easy)
print(hard)

"""
# query data to mysql
country = ['Thai','Japan','Korea','Australia']
cityT = ['Phitsanulok','Bangkok','Chiangmai']
cityJ = ['Tokyo','Nagoya','Tsushima']
cityK = ['Busan','Jeju','Seoul']
cityA = ['Sydney','Perth','Darwin']



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="test"
)

mycursor = mydb.cursor()

for i in range(200):
    test = []
    test.append(random.choice(country))
    if "Thai" in test:
        test.append(random.choice(cityT))
        money = random.randint(100000,2000000)
        test.append(money)
        paid = random.randint(100000,1000000)
        while paid > money:
            paid = random.randint(100000, 1000000)
        test.append(paid)
    elif "Japan" in test:
        test.append(random.choice(cityJ))
        money = random.randint(100000, 2000000)
        test.append(money)
        paid = random.randint(100000, 1000000)
        while paid > money:
            paid = random.randint(100000, 1000000)
        test.append(paid)
    elif "Korea" in test:
        test.append(random.choice(cityK))
        money = random.randint(100000, 2000000)
        test.append(money)
        paid = random.randint(100000, 1000000)
        while paid > money:
            paid = random.randint(100000, 1000000)
        test.append(paid)
    elif "Australia" in test:
        test.append(random.choice(cityA))
        money = random.randint(100000, 2000000)
        test.append(money)
        paid = random.randint(100000, 1000000)
        while paid > money:
            paid = random.randint(100000, 1000000)
        test.append(paid)

    sql = "INSERT INTO test1 (country, city, money, paid) VALUES (%s, %s, %s, %s)"
    val = tuple(test)
    mycursor.execute(sql, val)

    mydb.commit()
"""
