# 시간초과가 계속나서 검색해봄
# 1시간
def solution(phone_book):
    answer = True
    hass = {}
    for pn in phone_book:
        if pn not in hass:
            hass[pn] = 1
    for pn in phone_book:
        tmp = ''
        for n in pn: # len(pn) <= 20
            tmp += n
            if pn != tmp and tmp in hass:
                answer = False
    return answer

# ["119", "97674223", "1195524421"]

# ["119", "1195524421", "97674223"]
['1', '1', '9']
['9', '7', '6']

bool solution(vector<string> phone_book) {
    sort(phone_book.begin(), phone_book.end());
    for (int i=1; i<phone_book.size(); i++) {
        string& l = phone_book[i-1];
        string& r = phone_book[i];
        if (l.size() > r.size()) continue;
    	if (strncmp(l.c_str(), r.c_str(), l.size()) == 0)
            return false;
    }
    return true;
}

def solution(phone_book):
    phone_book.sort()
    for i in range(1, len(phone_book)):
        l = phone_book[i-1]
        r = phone_book[i]
        if len(l) > len(r):
            continue
        if l == r[:len(l)]:
            return False
    return False