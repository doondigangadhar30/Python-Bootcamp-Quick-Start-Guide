def calculate_love_score(s,m):
    t = r = u = l = o = v = e = 0
    for word in s,m:
        for letter in word:
            if letter == 't' or letter == 'T':
                t+=1
            if letter == 'r' or letter == 'R':
                r+=1
            if letter == 'u' or letter == 'U':
                u+=1
            if letter == 'l' or letter == 'L':
                l+=1
            if letter == 'o' or letter == 'O':
                o+=1
            if letter == 'v' or letter == 'V':
                v+=1
            if letter == 'e' or letter == 'E':
                e+=1
    print(f"{t+r+u+e}{l+o+v+e}")
calculate_love_score("Kanye West", "Kim Kardashian")
