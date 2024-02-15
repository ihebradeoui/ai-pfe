import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from time import time , ctime

cred = credentials.Certificate("face-recognition-1db25-firebase-adminsdk-4hcad-0373abc513.json")

default_app = firebase_admin.initialize_app(cred, {
	'databaseURL':"https://face-recognition-1db25-default-rtdb.firebaseio.com/"
	})
ref = db.reference("/")
print (ref.get())
ref.set({
	"people detected":
	{
		"iheb":ctime(time())
	}
})

"""
data={"content":"iheb detected"}
db.push(data)
"""