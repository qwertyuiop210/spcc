#how to run:
#first load the file in swi-prolog and then write the command:
#start.



start :-
    Board = [e,e,e,e,e,e,e,e,e],
    play(Board).

display([A,B,C,D,E,F,G,H,I]) :-
    write(A), write(' | '), write(B), write(' | '), write(C), nl,
    write('---------'), nl,
    write(D), write(' | '), write(E), write(' | '), write(F), nl,
    write('---------'), nl,
    write(G), write(' | '), write(H), write(' | '), write(I), nl,nl.

play(Board) :-
    display(Board),
    check_game(Board), !.

play(Board) :-
    player_move(Board, NewBoard),
    display(NewBoard),
    ( check_game(NewBoard) ->
        true
    ;
        computer_move(NewBoard, FinalBoard),
        play(FinalBoard)
    ).

check_game(Board) :-
    win(Board, x),
    write('Player wins!'), nl.

check_game(Board) :-
    win(Board, o),
    write('Computer wins!'), nl.

check_game(Board) :-
    \+ member(e, Board),
    write('Game Draw!'), nl.

player_move(Board, NewBoard) :-
    write('Enter position (1-9): '),
    read(Pos),
    ( move(Board, Pos, x, NewBoard) ->
        true
    ;
        write('Invalid move! Try again.'), nl,
        player_move(Board, NewBoard)
    ).

computer_move(Board, NewBoard) :-
    best_move(Board, Pos),
    write('Computer chooses position: '), write(Pos), nl,
    move(Board, Pos, o, NewBoard).

move(Board, Pos, Player, NewBoard) :-
    integer(Pos),
    Pos >= 1, Pos =< 9,
    nth1(Pos, Board, e),
    replace(Board, Pos, Player, NewBoard).

replace([_|T],1,X,[X|T]).
replace([H|T],Pos,X,[H|R]) :-
    Pos > 1,
    Pos1 is Pos - 1,
    replace(T,Pos1,X,R).

win([P,P,P,_,_,_,_,_,_],P).
win([_,_,_,P,P,P,_,_,_],P).
win([_,_,_,_,_,_,P,P,P],P).
win([P,_,_,P,_,_,P,_,_],P).
win([_,P,_,_,P,_,_,P,_],P).
win([_,_,P,_,_,P,_,_,P],P).
win([P,_,_,_,P,_,_,_,P],P).
win([_,_,P,_,P,_,P,_,_],P).

best_move(Board, Pos) :-
    win_move(Board, o, Pos), !.

best_move(Board, Pos) :-
    win_move(Board, x, Pos), !.

best_move(Board, 5) :-
    nth1(5, Board, e), !.

best_move(Board, Pos) :-
    nth1(Pos, Board, e).

win_move(Board, Player, Pos) :-
    nth1(Pos, Board, e),
    move(Board, Pos, Player, NewBoard),
    win(NewBoard, Player).
