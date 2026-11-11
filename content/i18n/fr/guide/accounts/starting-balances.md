---
title: Soldes de départ et ajustements
summary: Comment fonctionne le chiffre d'ouverture d'un compte et comment le corriger.
order: 60
---

# Soldes de départ et ajustements

Un solde initial est le chiffre que vous saisissez pour un compte quand vous apportez ses livres dans Damla. Il dit où se trouvait le compte quand vous avez commencé, pour que rien d'avant ce jour n'ait à être saisi. Un ajustement est une écriture que Damla rédige pour que vos livres s'accordent avec ce que dit votre banque ou un relevé. Les deux apparaissent comme des lignes grises dans Activité, sans signe plus ni moins : ils ne sont ni un revenu ni une dépense, donc ils ne changent jamais ce que vos rapports disent que vous avez gagné ou dépensé.

## Quand l'utiliser

- Vous ajoutez un compte bancaire, une épargne, un portefeuille, une carte ou un prêt et saisissez son solde du jour. Si ce chiffre n'est pas zéro, Damla l'enregistre comme solde initial du compte.
- Vous importez un relevé et tout l'argent n'a pas été capturé transaction par transaction — une carte que vous avez commencée à suivre au milieu d'un cycle, ou une alerte bancaire manquée. Damla comptabilise la différence comme un ajustement.
- Un chiffre dans vos livres ne correspond pas à l'application de votre banque, et vous voulez le remettre en accord.
- Vous voulez voir les corrections que Damla a apportées à ses livres.

## Étape par étape

1. Ouvrez Activité, la liste de chaque transaction.
2. Touchez **Filtrer** et choisissez **Soldes de départ** pour voir les chiffres d'ouverture, ou **Ajustements** pour voir les lignes que Damla a rédigées : ses corrections, avec les chiffres d'ouverture parmi elles.
3. Lisez une ligne de solde initial : elle porte le nom du compte, et la courte ligne en dessous dit **Solde initial**. Là où Damla a corrigé le coût d'un titre, la ligne dit **Coût corrigé** et nomme le titre à la place.
4. Lisez une ligne d'ajustement : elle s'intitule **Ajustement**, et la courte ligne en dessous nomme le compte et la raison que Damla a rédigée.

Pour remettre un compte en accord, la correction est toujours une écriture, jamais un chiffre que vous retapez. Mettez le compte à jour avec **Mettre à jour depuis des captures d’écran** en utilisant l'application de votre banque, ou importez un relevé et laissez Damla rapprocher. Il n'y a aucun champ qui écrase le solde d'un compte que vous utilisez déjà ; Damla rédige l'écriture de correction pour vous.

> **Note:** Chaque montant dans les livres de Damla circule entre deux endroits. Un solde initial ou un ajustement prend la différence d'un compte réservé nommé **Soldes d'ouverture**. C'est pourquoi il peut se situer en dehors des dépenses et des revenus sans que rien soit compté deux fois.

## Bon à savoir

### Pourquoi les soldes de départ sont masqués

Les soldes de départ sont masqués de la liste Activité ordinaire, parce qu'ils font partie de la configuration et non de quelque chose qui s'est passé. Une recherche, ou le choix d'un compte dans le même menu **Filtrer**, les montre à nouveau.

### Les ajustements ont des raisons en mots simples

La courte ligne d'un ajustement nomme le compte et la raison, par exemple « Solde reporté » ou « À jour du relevé ». Damla enregistre chaque raison avec le préfixe réservé « Rapprochement : » et laisse ce préfixe de côté dans la liste. L'écriture est aussi marquée comme rédigée par un import, pour que Damla puisse reconnaître ses propres ajustements plus tard. Les ajustements rédigés par des versions plus anciennes de l'application, qui utilisaient les mêmes mots sans le préfixe, sont reconnus aussi.

### Un import de relevé range les ajustements de sa période

Quand vous importez un relevé qui indique un solde de clôture, Damla rapproche le compte :

- Les ajustements antérieurs à l'intérieur de la période du relevé sont supprimés.
- Au plus deux nouveaux sont ajoutés : un pour que les livres avant la période égalent le solde d'ouverture du relevé, et un pour tout ce qui manque encore à la fin.
- Ensuite vos livres correspondent aux soldes d'ouverture et de clôture du relevé, et chaque transaction est comptée une fois.

Si un relevé n'indique pas de solde de clôture, rien n'est rapproché : sans ce chiffre il n'y a rien à quoi rapprocher. Si chaque ligne du relevé est déjà enregistrée, le bouton d'import lit **Rapprocher avec le relevé**, et le même rangement a quand même lieu.

> **Note:** Une carte doit de l'argent en deux parties : le relevé que votre banque a déjà émis, et ce que vous avez dépensé depuis. **Rapprochement : dernier relevé tel qu'indiqué par la banque** et **Rapprochement : dépensé depuis le dernier relevé, tel qu'indiqué par la banque** sont les mots réservés de Damla pour cette répartition, rédigés quand les chiffres d'une carte sont apportés depuis une capture d'écran de l'application de votre banque. Quand vous définissez plutôt le montant restant à payer dans les **Détails** d'une carte, la répartition est rédigée sous le même préfixe réservé. Dans les deux cas, le total que la carte doit reste tel quel.

> **Limit:** Damla compte ces lignes dans le solde d'un compte et dans vos prévisions, mais jamais comme dépense ou revenu dans vos rapports.

## En rapport

- [La liste Activité](/guide/recording/the-activity-list/)
- [Importer un relevé](/guide/capture/importing-statements/)
- [La page Comptes](/guide/accounts/accounts-page/)
