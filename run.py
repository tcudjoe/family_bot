from bot.messaging import send_msg

recipient_numbers = [
    "+31621608606",
    "+31615364792",
    "+31648423643",
    "+31621226967"
]

message = "Hello family, I am your agenda bot! You will give me your weekly events and I will spew them out according to the days. This way, all of you know eachothers whereabouts, and agendas."
if __name__ == "__main__":
    for number in recipient_numbers:
        send_msg(number, message)
        print(f"Message sent to {number}")
