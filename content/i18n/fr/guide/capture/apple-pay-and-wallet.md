---
title: Paiements Apple Pay et Wallet
summary: Ajoutez les paiements par carte au moment où ils ont lieu.
order: 40
---

# Paiements Apple Pay et Wallet

Quand vous payez avec Apple Pay ou en approchant votre carte, Wallet est informé du paiement immédiatement. Une automatisation Transaction Wallet envoie chaque paiement à Damla au moment où il a lieu, afin qu'il soit enregistré pour vous.

## Quand l'utiliser

- Vos cartes sont ajoutées à Apple Wallet et Damla doit enregistrer chaque paiement au fur et à mesure que vous le faites.
- Le message de votre banque au sujet du paiement arrive en retard, ou pas du tout, et vous voulez quand même qu'il soit enregistré.
- Vous voulez que le commerçant soit enregistré tel que Wallet le rapporte.

## Quelles actions utiliser

Toutes deux sont des actions de Damla dans l'app Shortcuts, et toutes deux font le même travail :

- **Ajouter à Damla**, avec son champ Texte réglé sur une phrase d'une seule ligne à propos du paiement et son champ Source réglé sur Paiement Wallet.
- **Ajouter un paiement par carte à Damla**, qui prend le commerçant, le montant et la carte directement dans la transaction Wallet.

Le montant arrive avec sa devise déjà incluse, il n'y a donc pas de champ de devise séparé et aucune conversion n'est devinée.

## Étape par étape

Une automatisation par carte, pour les cartes que vous avez ajoutées à Apple Wallet.

1. Ouvrez Damla, puis Réglages, puis Messages et relevés de la banque, puis Automatisations (Shortcuts).
2. Sous « Paiements Apple Pay », tapez les 4 derniers chiffres de votre carte et touchez Ajouter.
3. Touchez l'entrée de la carte dans la liste pour voir les étapes exactes la concernant. Vous pouvez copier les étapes, ou copier une invite à coller dans Apple Intelligence de l'app Shortcuts.
4. Ouvrez Shortcuts, touchez Automatisation, puis le bouton plus, puis choisissez Transaction Wallet et sélectionnez la carte.
5. Choisissez Exécuter immédiatement, puis Suivant.
6. Choisissez Nouvelle automatisation vierge, touchez Ajouter une action, cherchez **Ajouter à Damla** et sélectionnez-la.
7. Réglez son champ Texte sur la phrase que les étapes vous montrent : *Achat de [Montant] avec la carte se terminant par (vos chiffres) chez [Commerçant].* Damla a déjà écrit les chiffres de votre carte dans cette phrase, il ne reste donc que **Montant** et **Commerçant** entre crochets.
8. Touchez le champ Texte et insérez le Montant et le Commerçant de la transaction Wallet là où se trouvent les crochets.
9. Réglez Source sur Paiement Wallet.
10. Touchez Terminé.

> **Tip:** La phrase nomme la carte par ses chiffres, de la même manière qu'un texto de banque. Si les chiffres correspondent aux derniers chiffres que vous avez enregistrés pour cette carte dans ses détails de compte, Damla classe le paiement sous celle-ci immédiatement.

Si vous préférez, utilisez l'action **Ajouter un paiement par carte à Damla** au lieu de Ajouter à Damla. Ses trois champs — Commerçant, Montant et Carte — prennent leurs valeurs dans la transaction Wallet.

## Ce qui advient de chaque paiement

- Un paiement sur une carte que Damla connaît est ajouté comme transaction immédiatement.
- Un paiement sur une carte inconnue, ou tout ce que Damla ne peut pas lire, attend dans la Boîte de réception, où un seul geste suffit.
- Si le même paiement parvient aussi à Damla par un texto de la banque, il n'est enregistré qu'une fois. Un second rapport avec un nom de boutique correspondant reçoit la réponse **Déjà dans Damla**. Si la boutique est nommée différemment et que le rapport arrive dans les 15 minutes suivant le premier, le second rapport attend dans la Boîte de réception comme doublon possible, pour que vous puissiez l'écarter.

> **Note:** Quand le téléphone est verrouillé, les livres ne peuvent pas être lus, donc Damla conserve le paiement et l'ajoute la prochaine fois que vous déverrouillez l'app.

## Bon à savoir

- **Envoyez un paiement test** après la configuration. L'écran Automatisations montre quand le dernier message est parvenu à Damla, et **Alertes récentes** liste chacune avec ce qui a été fait. S'il n'est pas arrivé, l'automatisation n'est probablement pas réglée sur Exécuter immédiatement.
- **Les chiffres comptent.** Une carte dont les derniers chiffres sont enregistrés dans ses détails de compte est reconnue automatiquement. Une carte que Damla ne connaît pas attend que vous lui disiez laquelle c'était ; vous ne le faites qu'une fois par carte.
- **Si Damla est en lecture seule** parce qu'un essai ou un abonnement a pris fin, l'action le dit et rien n'est ajouté tant que vous ne vous abonnez pas à nouveau.

## À voir aussi

- [Textos et e-mails de la banque](/guide/capture/bank-texts-and-emails/)
- [Comment fonctionne la capture automatique](/guide/capture/how-automatic-capture-works/)
- [La boîte de réception](/guide/recording/the-inbox/)
- [Cartes de crédit](/guide/accounts/credit-cards/)
