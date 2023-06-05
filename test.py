import os
import mysql.connector
import subprocess
#Connect to SDK
PSDK_APPID="anggi"
PSDK_SAFE="dummy"
PSDK_FOLDER="root"
PSDK_OBJECT="anggi-test"
PSDK_PATH="C:\\Program Files (x86)\\CyberArk\\ApplicationPasswordSdk\\CLIPasswordSDK.exe"

if os.name == 'nt':
    parameter = '/'
else:
    parameter = '-'

password = subprocess.run([PSDK_PATH,'GetPassword' , parameter + 'p' ,'AppDescs.AppID='+ PSDK_APPID +'',  parameter + 'p', 'Query=safe=' + PSDK_SAFE + ';Folder=' + PSDK_FOLDER + ';Object=' + PSDK_OBJECT + '',  parameter + 'p', 'RequiredProps=*' , parameter + 'o', 'Password'],stdout=subprocess.PIPE )
str_password = password.stdout
str_password = str_password.strip()
str_password=str(str_password,'utf-8')

print ("password dari AAM")
print("output:", str_password)

username = subprocess.run([PSDK_PATH,'GetPassword' , parameter + 'p' ,'AppDescs.AppID='+ PSDK_APPID +'',  parameter + 'p', 'Query=safe=' + PSDK_SAFE + ';Folder=' + PSDK_FOLDER + ';Object=' + PSDK_OBJECT + '',  parameter + 'p', 'RequiredProps=*' , parameter + 'o', 'Passprops.Username'],stdout=subprocess.PIPE )
str_username = username.stdout
str_username = str_username.strip()
str_username=str(str_username,'utf-8')

print ("username dari AAM")
print("output:", str_username)

#connection string
mydb = mysql.connector.connect(
  host="localhost",
  user=str_username,
  password=str_password,
  database="world"
)


mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM country")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)