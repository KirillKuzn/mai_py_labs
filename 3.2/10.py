def main():
    al = {
        'А': 'A', 'Б': 'B', 'В': 'V', 'Г': 'G', 'Д': 'D', 'Е': 'E', 'Ё': 'E', 'Ж': 'Zh', 
        'З': 'Z', 'И': 'I', 'Й': 'I', 'К': 'K', 'Л': 'L', 'М': 'M', 'Н': 'N', 'О': 'O', 
        'П': 'P', 'Р': 'R', 'С': 'S', 'Т': 'T', 'У': 'U', 'Ф': 'F', 'Х': 'Kh', 'Ц': 'Tc', 
        'Ч': 'Ch', 'Ш': 'Sh', 'Щ': 'Shch', 'Ы': 'Y', 'Э': 'E', 'Ю': 'Iu', 'Я': 'Ia'
    }
    al['Ъ'] = ''
    al['Ь'] = ''
    alm = {}
    for le in al:
        alm[le.lower()] = al[le].lower()
    for le in alm:
        al[le] = alm[le]
    s = input()
    ans = ''
    for le in s:
        if le in al:
            ans += al[le]
        else:
            ans += le
    print(ans)


if __name__ == "__main__":
    main()