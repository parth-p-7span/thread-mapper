
def beautify_number(number):
    emojis = ['0⃣', '1⃣', '2⃣', '3⃣', '4⃣', '5⃣', '6⃣', '7⃣', '8⃣', '9⃣']
    e_string = ""
    for i in str(number):
        e_string += emojis[int(i)]
    return e_string
