% Oded Ofek 215348145
% Ziv Farajun 323920603
%section 1: - אבא
father(X,Y):-parent(X,Y),male(X).
%section 2: - אמא
mother(X,Y):-parent(X,Y),female(X).

%section 1: - אבא
father(X,Y):-parent(X,Y),male(X).
%section 2: - אמא
mother(X,Y):-parent(X,Y),female(X).
%section 3: - בן
son(X,Y):-parent(Y,X),male(X).
%section 4: - בת
daughter(X,Y):-parent(Y,X),female(X).
%section 5: - סבא
grand_father(X,Z):-father(X,Y),parent(Y,Z).
%section 6: - סבתא
grand_mother(X,Z):-mother(X,Y),parent(Y,Z).
%section 7: - נכד
grand_son(X,Z):-son(X,Y),parent(Z,Y).
%section 8: -נכדה 
granddaughter(X,Z):-daughter(X,Y),parent(Z,Y).
%section 9: - אחים 
sibling(X,Y):-father(Z,X),father(Z,Y),diff(X,Y).   
sibling(X,Y):-mother(W,X),mother(W,Y),diff(X,Y).
%section 10: - דוד בלי קשר דם
uncle_in_law(X,Y):-parent(Z,Y),sibling(W,Z),married(X,W),male(X).
%section 11: - בן דודה
cousin(X,Y):-mother(Z,X),parent(W,Y),sibling(W,Z).     % בן דודה עם קשר דם 
cousin(X,Y):-mother(Z,X),married(W,Z),sibling(W,U),parent(U,Y). % בן דודה בלי קשר דם 
%section 12: -גיס 
brother_in_law(X,Y):-married(W,Y),sibling(W,X),male(X),male(W),female(Y). % אחי בעלה  
brother_in_law(X,Y):-married(Y,W),sibling(W,X),male(X),female(W),male(Y). % אחי אישתו
brother_in_law(X,Y):-married(X,W),sibling(W,Y),male(X),male(Y),female(W). % בעלה של אחותו
brother_in_law(X,Y):-married(X,W),sibling(W,Y),male(X),female(W),female(Y). % בעלה של אחותה
brother_in_law(X,Y):-married(X,W),sibling(W,Z),married(Z,Y),male(X),female(W),male(Z),female(Y). % בעל אחותו של בעלה
brother_in_law(X,Y):-married(X,W),sibling(W,Z),married(Y,Z),male(X),female(W),male(Y),female(Z). % בעל אחותה של אשתו  
%section 13: אחיינית 
niece(X,Y):-daughter(X,W),sibling(W,Y).
%section 12: -בן דוד מדרגה שנייה 
second_cousin(X,Y):-parent(W,X),parent(Z,W),parent(U,Y),parent(F,U),sibling(F,Z).


%section1 - reverse.
reverse([],[]).% הרשימה הריקה היא ההפך של עצמה
reverse([H|T],R) :- my_reverse(T,Z1), append(Z1,[H],Z).% נקרא שוב לרוורס. ונוסיף את הראש לרשימה החדשה

%section2 -member
my_member(X, [X|_]).%  אם המשתנה שאנו מחפשים הוא ראש הרשימה נסיים את התוכנית בנכון 
my_member(X, [_|T]) :- my_member(X, T).  %אם נשארו איברים, אז נשלח את הזנב ואת האיבר שוב בריקורסיה

%section3-palindrom
palindrome([]).  %אם הרשימה ריקה היא עדיין פולינדרום
palindrome([_]). % אם יש רק איבר אחד ברשימה היא פולינדרום
palindrome([X|Xs]) :-my_reverse([X|Xs], [X|Xs]).   %בודק אם הפונקציה היא ההפוכה של עצמה, אם כן היא פולינדרום

%section4-sorted
my_sorted([]).% ריק זה ממויין 
my_sorted([_]). % איבר אחד זה ממויין
my_sorted([X,Y|Rest]) :- X =< Y, my_sorted([Y|Rest]). %בודק אם האיבר הראשון קטן מהשני, אם כן ממשיך לבדוק מהשני והלאה עד לזימון הפונ' עם איבר בודד

%question 1 א:
scum(N,0):-N=0. % תנאי עצירה- הפונקציה מגיעה ל-0
scum(N,RES):- N1 is N-1, scum(N1,RES1), RES is RES1 + N.% רקורסיה, נחסר ב1 את המספר עד שנגיע לתנאי העצירה ונחבר כשהפונקציה תחזור

%question 1 ב:
sumDigits(NUM,NUM):-NUM<10. % תנאי עצירה- כאשר המספר חד ספרתי
sumDigits(NUM,SUM):-N1 is NUM//10 ,sumDigits(N1,SUM1), SUM is SUM1 + NUM mod 10.% רקורסיה, נגלח את הספרה השמאלית של המספר עד שנגיע לתנאי העצירה ונחבר כשהפונקציה תחזור

%question 2 א:
split(N,[]):-N=0.% תנאי עצירה- כאשר עברנו על כל הספרות של המספר
split(N,RES):-D is N mod 10 ,N1 is N//10, split(N1,RES1) ,append(RES1,[D] ,RES).% ריקורסיה- ניקח את הספרה האחרונה כנתון ואת המספר בלעדיה, נכניס לרשימה באמצעות ריקורסיה בכל פעם את האות האחרונה

%question 2 ב:
create([], 0).% תנאי עצירה-כאשר הרשימה נגמר.
create([H|T],N):- create(T,N1), N is H + N1 * 10.% .ריקורסיה- בכל קריאה נזמן את הפונקציה שוב עם הרשימה בלי הראש עד שנגיע לתנאי העצירה ואז נוסיף למשתנה את הראש הנוכחי עם מכפלת שאר המספר ב10

%question 3 א:
intersection([], _, []).% תנאי עצירה-כאשר נסיים לעבור על כל הרשימה
intersection([X|Rest], L2, [X|Z]) :-member(X, L2),intersection(Rest, L2, Z).% אם מצאנו איברים זהים אז נכניס את האיבר ונמשיך בריקורסיה
intersection([_|Rest], L2, Z) :-intersection(Rest, L2, Z). % אם היאבר לא זהה נמשיך באמצעות רקורסיה לאיבר הבא 

%question 3 ב:
minus([], _, []).% תנאי עצירה-כאשר נסיים לעבור על כל הרשימה
minus([X|Rest], L2, Z) :-member(X, L2),minus(Rest, L2, Z).%אם מצאנו איברים שונים נכניס את האיבר ונמשיך בריקורסיה
minus([X|Rest], L2, [X|Z]) :-minus(Rest, L2, Z). % 