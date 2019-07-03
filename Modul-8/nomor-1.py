def cetakHexa(angka):
    digits="0123456789ABCDEF"
    stack=Stack()
    st=""
    if angka==0:
        stack.push(0)
    while angka>0:
        digit=angka%16
        stack.push(digits[digit])
        angka=angka//16
    while len(stack)>0:
        st+=stack.pop()
    print(st)
cetakhexa(40)
