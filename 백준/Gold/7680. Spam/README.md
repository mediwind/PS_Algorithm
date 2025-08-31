# [Gold V] Spam - 7680 

[문제 링크](https://www.acmicpc.net/problem/7680) 

### 성능 요약

메모리: 32412 KB, 시간: 112 ms

### 분류

다이나믹 프로그래밍, 문자열

### 제출 일자

2025년 8월 31일 22:55:15

### 문제 설명

<p>To thwart content-based spam filters, spammers often modify the text of a spam email to prevent its recognition by automatic filtering programs. For any plain text string s (containing only upper-case letters), let Φ(s) denote the string obtained by substituting each letter with its “spam alphabet” equivalent:</p>

<pre>A 4 (four)
B |3 (pipe three)
C ( (left-parenthesis)
D |) (pipe right-parenthesis)
E 3 (three)
F |= (pipe equals)
G 6 (six)
H # (pound)
I | (pipe)
J | (underscore pipe)
K |< (pipe less-than)
L | (pipe underscore)
M |\/| (pipe backslash forward-slash pipe)
N |\| (pipe backslash pipe)
O 0 (zero)
P |0 (pipe zero)
Q (,) (left-parenthesis comma right-parenthesis)
R |? (pipe question-mark)
S 5 (five)
T 7 (seven)
U | | (pipe underscore pipe)
V \/ (backslash forward-slash)
W \/\/ (backslash forward-slash backslash forward-slash)
X >< (greater-than less-than)
Y -/ (minus forward-slash)
Z 2 (two)</pre>

<p>In this scheme, any plain text message s corresponds to exactly one spam-encoded message Φ(s). The reverse, however, is not necessarily true: a spam-encoded message may correspond to more than one plain text message.</p>

<p>Given a plain text message s, your goal is to determine the number of unique plain text messages whose spam encoding is Φ(s).</p>

### 입력 

 <p>The input test file will contain multiple test cases. Each test case consists of a single line containing a plain text string s containing from 1 to 100 upper-case letters. The end-of-file is denoted by a single line containing the word “end”.</p>

### 출력 

 <p>For each test case, print the number of unique plain text messages (including the original message) whose spam encoding is Φ(s). The number of unique plain text messages is guaranteed to be no greater than 1,000,000,000.</p>

