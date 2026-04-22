#how to run:
#first load the file in swi-prolog and then write the command:
#start.



:- dynamic(fact/1).

rule(malaria) :-
    fact(fever),
    fact(headache),
    fact(vomiting),
    fact(joint_pain).

rule(typhoid) :-
    fact(fever),
    fact(abdominal_pain),
    fact(headache),
    fact(vomiting).

rule(dengue) :-
    fact(fever),
    fact(joint_pain),
    fact(rash),
    fact(headache).

ask(S) :-
    write('Do you have '), write(S), write('? (yes/no): '),
    read(R),
    (R == yes -> assertz(fact(S)) ; true).

get_facts :-
    ask(fever),
    ask(headache),
    ask(vomiting),
    ask(joint_pain),
    ask(rash),
    ask(abdominal_pain).

forward_chain :-
    rule(D),
    write('Derived Disease: '), write(D), nl,
    !.

forward_chain :-
    write('No disease derived.'), nl.

start :-
    get_facts,
    forward_chain,
    clear.

clear :-
    retract(fact(_)), fail.
clear.
