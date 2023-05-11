
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

cred = credentials.Certificate("serviceAccountKey.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': ""
})

ref = db.reference('Students')

data = {
"621104":
        {
            "name": "Aakash",
            "major": "Engineering",
            "starting_year": 2022,
            "total_attendance": 5,
            "standing": "A",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
"524211":
        {
            "name": "Sandeep",
            "major": "Engineering",
            "starting_year": 2022,
            "total_attendance": 11,
            "standing": "A",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "321123":
        {
            "name": "Shiva",
            "major": "Engineering",
            "starting_year": 2020,
            "total_attendance": 16,
            "standing": "B",
            "year": 3,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "852741":
        {
            "name": "Emly Blunt",
            "major": "Economics",
            "starting_year": 2021,
            "total_attendance": 12,
            "standing": "B",
            "year": 1,
            "last_attendance_time": "2022-12-11 00:54:34"
        },
    "963852":
        {
            "name": "Elon Musk",
            "major": "Physics",
            "starting_year": 2020,
            "total_attendance": 7,
            "standing": "G",
            "year": 2,
            "last_attendance_time": "2022-12-11 00:54:34"
        }
}

for key, value in data.items():
    ref.child(key).set(value)
