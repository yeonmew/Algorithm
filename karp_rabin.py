alphabet = 256
 
def search(pat, txt, q): # q는 첫번째 값
    M = len(pat)
    N = len(txt)
    i = 0
    j = 0
    p = 0    # 패턴의 해쉬값
    t = 0    # txt의 해쉬값
    re = 1
 
    for i in range(M-1):
        re = (re * alphabet)% q
 
    for i in range(M): # 문장의 패턴과 첫번째 해쉬 값 계산
        p = (alphabet * p + ord(pat[i]))% q
        t = (alphabet * t + ord(txt[i]))% q
 
    for i in range(N-M + 1): # 문장의 패턴을 하나씩 검토
        # Check the hash values of current window of text and
        # pattern if the hash values match then only check
        # for characters on by one
        if p == t:
            # Check for characters one by one
            for j in range(M):
                if txt[i + j] != pat[j]:
                    break
 
            j+= 1
            # if p == t and pat[0...M-1] = txt[i, i + 1, ...i + M-1]
            if j == M:
                print ("Pattern found at index " + str(i))
 
        # Calculate hash value for next window of text: Remove
        # leading digit, add trailing digit
        if i < N-M:
            t = (d*(t-ord(txt[i])*h) + ord(txt[i + M]))% q
 
            # We might get negative values of t, converting it to
            # positive
            if t < 0:
                t = t + q
 
# Driver program to test the above function
txt = "mew comento mew"
pat = "mew"
q = 101 # A prime number
search(pat, txt, q)
 
# This code is contributed by Bhavya Jain