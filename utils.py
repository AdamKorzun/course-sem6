import json
import os
import mysql.connector
import time
mydb = mysql.connector.connect(
  host="localhost",
  user="course",
  password="password",
  database='coursesem6'
)
cursor = mydb.cursor()
def load_sha_hashes():
    with open('data/SHA1 HASHES.json', 'r') as f:
        dataset = json.loads(f.read())['data']
    data = []
    for i in dataset:
        data.append((i['name'], None, i['hash']))
    # print(data)
    cursor.executemany('INSERT INTO VIRUS (name, md5_hash, sha_hash)  VALUES (%s, %s, %s)', data)
    mydb.commit()


def load_md5_hashes():
    with open("data/MD5 Virus Hashes.txt",'r') as f:
        lines = [line.rstrip() for line in f]
    data = []
    for i in lines:
        data.append((None,  i, None))
    # print(data)
    number_of_arrays = 100
    data_split = []
    one_dataset_size = int(len(data) / number_of_arrays)
    for i in range(number_of_arrays):
        data_split.append(data[i * one_dataset_size:((i+1) * one_dataset_size)])
    k = 0
    for i in data_split:
        # print(i)
        cursor.executemany('INSERT INTO VIRUS (name, md5_hash, sha_hash)  VALUES (%s, %s, %s)', i)
        mydb.commit()

        print('%s inserted', k)
        k+=1
        time.sleep(2)

if __name__ == '__main__':
    # load_sha_hashes()
    # load_md5_hashes()
