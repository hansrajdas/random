import requests


def get_data():
    data = requests.get("https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id=294&date=08-05-2021")
    d = data.json()

    centers = d['centers']
    for centre in centers:
        for session in centre['sessions']:
            if session['min_age_limit'] == 18 and session['available_capacity'] == 0:
                print(centre['name'], centre['address'], session['date'], session['min_age_limit'], session['available_capacity'])
        

def main():
    get_data()

if __name__ == '__main__':
    main()
