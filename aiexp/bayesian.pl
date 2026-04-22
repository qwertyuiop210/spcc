#how to run:
#first load the file in swi-prolog and then write the command:
#normalize([cloudy,humidity]).
#predict([cloudy,humidity]).



prior(sunny, 0.5).
prior(rainy, 0.3).
prior(cloudy, 0.2).

likelihood(cloudy, sunny, 0.2).
likelihood(cloudy, rainy, 0.7).
likelihood(cloudy, cloudy, 0.9).

likelihood(humidity, sunny, 0.3).
likelihood(humidity, rainy, 0.8).
likelihood(humidity, cloudy, 0.6).

compute_likelihood([], _, Acc, Acc).

compute_likelihood([E|Rest], Weather, Acc, Result) :-
    likelihood(E, Weather, L),
    NewAcc is Acc * L,
    compute_likelihood(Rest, Weather, NewAcc, Result).

posterior(Weather, EvidenceList, Posterior) :-
    prior(Weather, Prior),
    compute_likelihood(EvidenceList, Weather, 1.0, LikelihoodProduct),
    Posterior is Prior * LikelihoodProduct.

normalize(EvidenceList) :-
    posterior(sunny, EvidenceList, PSunny),
    posterior(rainy, EvidenceList, PRainy),
    posterior(cloudy, EvidenceList, PCloudy),
    Sum is PSunny + PRainy + PCloudy,
    NSunny is PSunny / Sum,
    NRainy is PRainy / Sum,
    NCloudy is PCloudy / Sum,
    write('Posterior Probabilities:'), nl,
    write('Sunny  = '), write(NSunny), nl,
    write('Rainy  = '), write(NRainy), nl,
    write('Cloudy = '), write(NCloudy), nl.

predict(EvidenceList) :-
    posterior(sunny, EvidenceList, PSunny),
    posterior(rainy, EvidenceList, PRainy),
    posterior(cloudy, EvidenceList, PCloudy),
    Max is max(PSunny, max(PRainy, PCloudy)),
    ( Max =:= PSunny -> Weather = sunny
    ; Max =:= PRainy -> Weather = rainy
    ; Weather = cloudy
    ),
    write('Predicted Weather: '),
    write(Weather), nl.
