            name = input('Type your full name: ').strip().title()
            bday_day = input('Insert your birthday day: ').strip()
            bday_month = input('Insert your birthday month: ').strip()
            bday_year = input('Insert your birthday year: ').strip()
            bday_date = f'{bday_day}/{bday_month}/{bday_year}'
            street = input('Insert your street name: ').strip().title()
            num = input('Insert your house number: ').strip().title()
            nbhood = input('Insert your neighborhood name: ').strip().title()
            city = input('Insert the city: ').strip().title()
            state = input('Insert the state acronym: ').strip().upper()
            address = f'{street}, {num} - {nbhood} - {city}/{state}'
            break #2
