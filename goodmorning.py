from twilio.rest import Client
import schedule
import requests
import time

# Twilio credentials
acoount_sid = ''
auth_token = 'your_auth_token'
twilio_phone_number = 'your_twilio_phone_number'
your_phone_number = 'your_phone_number'


#function to fetch a random Bible verse
def getRandomVerse():
    url = 'http://labs.bible.org/api/?passage=random&type=json'
    response = requests.get(url)
    if response.status_code == 200:
        verse_data = response.json()
        verse = verse_data['0']['text']
        reference = verse_data[0]['bookname'] + '-' + verse_data[0]['chapter'] + ':' + verse_data[0]['verse']
        return verse, reference
    else:
        print("Failed to fetch Bible Verse")
        return None, None
    


#function for sending good morning message
def send_good_morning_message():
    verse, reference = get_random_bible_verse()
    if verse and reference:
        client = Client(account_sid, auth_token)
        message_body = f"Good morning sunshine! Here's a Bible verse to help to you through the day:\n\n{verse}\n\n- {reference}"
        message = client.messages.create(
            body=message_body,
            from_=twilio_phone_number,
            to=your_phone_number
        )
        print('Message sent!')

    
#schedule the message to be sent every morning
schedule.every().day.at("06:00").do(send_good_morning_message)

while True:
    schedule.run_pending()
    time.sleep(1)