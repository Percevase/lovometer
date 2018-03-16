#include <iostream>
#include <string>
#include <cmath>
#include <cctype>
#include "unistd.h"


using namespace std;
void ToLower (string & Astring){
    for (char & letter : Astring){
        letter = tolower(letter);
    }
}

void presentation (){
	cout << "voici le lovover 9000 !" << endl;
	system ("timeout 1 > nul");
	cout << "pour savoir a quel point vous etes lie avec une une personne tapez votre nom et le sien !" << endl;
	system("timeout 1 > nul");
	cout << "la machine calculera automatiquement le pourcentage de compatibilite que vous avez avec cette personne !" << endl;
}

unsigned calcLove (const string & lover1, const string & lover2){
	float lovoScore = 0.0;
	const float KMaxLovoScore = lover1.length () + lover2.length ();

	if (lover1.length () == lover2.length ()){
		lovoScore = 0.75 * (lover1.length() + lover2.length ());
	}
	else if (lover1.length () > lover2.length ()){
		lovoScore = 0.75 * lover1.length ();
	}
	else{
		lovoScore = 0.75 * lover2.length ();
	}

	for (unsigned i (0); i < lover1.length (); ++i){
		for (unsigned j (0); j < lover2.length (); ++j){
			if (lover2[j] == lover1[i]){
                if (j == i){
                    lovoScore += 1;
                }
                else {
                    lovoScore = lovoScore + (1/fabs (j - i));
                }
			}
		}
	}

	if (lovoScore > KMaxLovoScore){
		lovoScore = lovoScore - 0.25 * KMaxLovoScore;
	}

	return int (lovoScore * 100 / KMaxLovoScore);
}

int main (){
	presentation ();
	string name1, name2;
	cout << "entrer votre nom: ";
	getline (cin, name1);
	cout << "entrer le nom de votre amour: ";
	getline (cin, name2);
	ToLower(name1);
	ToLower(name2);
	cout << "votre compatibilite avec " << name2 << " est de: " << calcLove(name1, name2) << "% !" << endl;
	return 0;
}
