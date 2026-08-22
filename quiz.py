l='o'
score = 0
while l != 'N':
    print('Quiz Mtk')

    x = float(input('1.) Berapa hasil dari 125 / 5 ? : '))
    if x == 25:
        score += 1
    else:
        pass

    y = float(input('2.) Berapa hasil dari 49 + 23 ? : ' ))
    if y == 72:
        score += 1
    else:
        pass

    z = float(input('3.) Berapa hasil dari 2^7 ? : '))
    if z == 128:
        score += 1
    else:
        pass

    v = float(input('4.) Berapa hasil dari 500 - 229 ? : '))
    if v == 271:
        score += 1
    else:
        pass

    b = float(input('5.) Berapa hasil dari 29 %(Modulo) 2 ? : '))
    if b == 1:
        score += 1
    else:
        pass

    n = float(input('6.) Berapa hasil dari 31 %(Modulo) 5 ? :'))
    if n == 1:
        score += 1
    else:
        pass

    m = float(input('7.) Berapa hasil dari 21 - 13 ? : '))
    if m == 8:
        score += 1
    else:
        pass

    a = float(input('8.) Berapa hasil dari 3^3 ? : '))
    if a == 27:
        score += 1
    else:
        pass

    s = float(input('9.) Berapa hasil dari 5 + 1234 ? : '))
    if s == 1239:
        score += 1
    else:
        pass

    d = float(input('10.) Berapa hasil dari 212 / 2 ? : '))
    if d == 106:
        score += 1
    else:
        pass

    if score >= 8:
        print(f"Nilai kamu yaitu {score} / 10")
        print('Kamu Lulus')

        l = input('Apakah mau ulang lagi [y/N]? :  ')
        if l == 'N':
            print('Terima Kasih')
            break
        elif l == 'y':
            print('Ok')
            continue

    if score < 8:
        print(f"Nilai kamu yaitu {score} / 10")
        print('Kamu Tidak Lulus')

        l = input('Apakah kamu mau coba lagi, atau tidak? [y/N] : ')
        if l == 'N':
            print('Terima Kasih')
            break
        elif l == 'y':
            print('Ok')
            continue
