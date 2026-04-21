# [Platinum III] Suluavaldised - 29868 

[문제 링크](https://www.acmicpc.net/problem/29868) 

### 성능 요약

메모리: 143948 KB, 시간: 2096 ms

### 분류

자료 구조, 누적 합, 세그먼트 트리

### 제출 일자

2026년 4월 21일 20:24:15

### 문제 설명

<p><em>Suluavaldiseks</em> nimetatakse sõnet, mis on saadud järgmiste reeglite abil:</p>

<ul>
	<li>$()$ on suluavaldis;</li>
	<li>kui $s$ on suluavaldis, siis ka $(s)$ on suluavaldis;</li>
	<li>kui $s$ ja $t$ on suluavaldised, siis ka $st$ on suluavaldis.</li>
</ul>

<p>Näiteks <code>()()</code>, <code>(())()</code> ja <code>(()())</code> on suluavaldised, aga <code>(()(</code>, <code>)(</code> ja <code>kala</code> ei ole.</p>

<p>Meil on antud sõne $A$ pikkusega $N$, mis koosneb ainult sümbolitest <code>(</code> ja <code>)</code>. Lisaks on antud $M$ päringut, millest igaüks on kujul:</p>

<blockquote>
<p>Antud $L$ ja $R$. Kas leidub selline $k$, et $L < k < R$ ning $A_L A_{L + 1} \ldots A_k$ ja $A_{k + 1} A_{k + 2} \ldots A_R$ on mõlemad suluavaldised? Väljasta <code>JAH</code>, kui leidub, ning <code>EI</code>, kui ei leidu.</p>
</blockquote>

<p>Sõne $A$ positsioonid on nummerdatud $1, \ldots, N$.</p>

### 입력 

 <p>Sisendi esimesel real on täisarvud $N$ ja $M$ ($2 \le N \le 10^6$, $1 \le M \le 10^6$) --- sisendsõne pikkus ja päringute arv.</p>

<p>Teisel real on sõne $A$: täpselt $N$ sümbolit, millest igaüks on <code>(</code> või <code>)</code>.</p>

<p>Järgmisel $M$ real on igaühel kaks tühikuga eraldatud täisarvu $L$ ja $R$ ($1 \le L < R \le N$), mis kirjeldavad päringuid.</p>

### 출력 

 <p>Väljundisse kirjutada päringute vastused, igaüks eraldi reale.</p>

