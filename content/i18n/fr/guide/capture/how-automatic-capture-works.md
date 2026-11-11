---
title: Comment fonctionne la capture automatique
summary: Textos, e-mails, paiements Wallet et relevés de la banque, et ce que Damla en fait.
order: 10
---

# Comment fonctionne la capture automatique

La capture automatique, c'est la façon dont un message de la banque devient une transaction sans que vous tapiez quoi que ce soit. Damla lit les textos, les e-mails, les paiements Wallet et les fichiers de relevés qui lui parviennent, détermine ce qu'est chacun d'eux, puis soit l'ajoute, soit vous pose la question, soit le laisse de côté.

## Comment les messages parviennent à Damla

iOS ne donne aux apps aucun accès aux messages ou au courrier, donc Damla ne les lit jamais de lui-même. Quelque chose ne parvient à Damla que lorsque vous l'envoyez, de l'une des trois façons suivantes :

- **Un raccourci que vous avez configuré** transmet chaque nouveau texto, e-mail ou paiement Wallet à Damla dès son arrivée.
- **La feuille de partage** : vous sélectionnez un message et le partagez vers Damla.
- **Le sélecteur de fichiers** : vous choisissez les fichiers de relevés à importer.

Tout est lu sur le téléphone. Rien n'est téléversé.

## Ce qui advient d'un message

Damla compare chaque message à la même liste de règles, dans cet ordre, et s'arrête à la première qui correspond.

1. **Les codes à usage unique et les codes d'approbation sont écartés.** Les mots du message ne sont jamais conservés, si bien qu'un code ne peut pas être relu plus tard. Tout ce qui reste est une ligne dans le journal disant « Code à usage unique : jamais conservé ».
2. **Un avis de facture est mémorisé comme une facture.** « Votre facture est prête » n'est pas un paiement : l'argent n'a pas bougé. Damla la conserve comme facture attendue, et le débit de carte qui la paie plus tard est la seule vraie transaction.
3. **Les publicités, les avis de limite et de taux, les rappels et les débits futurs annoncés sont écartés.** Ils mentionnent un montant, mais aucun argent n'a bougé. Quand un tel message parle d'argent, Damla note ses premiers mots dans le journal, pour que vous puissiez voir une erreur d'appréciation.
4. **Une alerte bancaire claire est ajoutée immédiatement.** Un achat, un remboursement ou un revenu dont les chiffres de carte ou de compte correspondent à l'un de vos comptes devient une transaction tout de suite. Les paiements par carte, les remboursements et les virements sont reconnus. La catégorie vient de la façon dont vous avez classé ce bénéficiaire auparavant, à défaut **Autre** pour les dépenses et **Autre revenu** pour l'argent entrant.
5. **Tout ce qui n'est pas clair attend dans la Boîte de réception**, où un seul geste suffit. Rien qui crée un engagement — une facture, un prêt, un plan de paiement échelonné — n'est ajouté sans votre confirmation.
6. **Un message qui ne parle pas du tout d'argent est écarté.** Il n'est ni conservé ni consigné, si bien qu'un message privé ne se retrouve jamais dans la boîte de réception ni dans le journal.

## Où vérifier ce qui s'est passé

- **Alertes récentes** (Réglages > Messages et relevés de la banque) est un journal des 50 dernières alertes, des plus récentes aux plus anciennes, chacune avec une brève raison : Ajoutée, En attente dans la boîte de réception (et pourquoi), Déjà enregistrée, Ignorée, ou une facture notée comme à venir. Si un message de la banque arrive et que rien n'apparaît ici, le raccourci ne s'est pas exécuté.
- **La Boîte de réception** apparaît sur Aujourd'hui sous la forme **N en attente de votre accord**. Touchez un élément pour l'ouvrir dans **Ajouter par une phrase**, où il est relu pour que vous puissiez le vérifier. Il quitte la Boîte de réception quand vous l'enregistrez, et **Abandonner** le retire sans rien ajouter.
- Une alerte sur laquelle Damla a agi peut être retirée : dans Alertes récentes, balayez la ligne vers la droite et touchez **Annuler**. La transaction qu'elle a ajoutée est supprimée, ou la facture qu'elle a notée est oubliée.

## Bon à savoir

- **La même alerte deux fois n'est ajoutée qu'une fois.** Un achat signalé à nouveau par le texto de la banque, son e-mail ou Wallet apparaît comme déjà enregistré. Un second signalement du même montant dans les minutes qui suivent attend dans la Boîte de réception pour que vous décidiez.
- **La première alerte d'une nouvelle carte attend dans la Boîte de réception**, car Damla ne connaît pas encore les derniers chiffres de cette carte. Complétez-la une fois et Damla les apprend.
- **Un message qui arrive pendant que le téléphone est verrouillé** attend, et est ajouté la prochaine fois que vous ouvrez l'app après avoir déverrouillé le téléphone. Si vos livres sont en lecture seule, il reste dans cette file d'attente jusqu'à ce que vous puissiez modifier à nouveau.
- **Un PDF de relevé** envoyé par un raccourci est mis en file d'attente. Aujourd'hui montre **N en attente d'examen** avec la mention « Relevés ou captures d'écran. Rien n'est ajouté tant que vous ne confirmez pas », et vous l'examinez avant tout ajout.
- **Là où le téléphone a Apple Intelligence**, le modèle peut seulement lire des champs depuis le texte. Chaque nombre et chaque nom qu'il renvoie doit figurer dans le texte, sinon il est ignoré, et ce qu'il lit n'est jamais enregistré sans que vous le voyiez.
- **La lecture se fait par la formulation et n'est pas parfaite.** Une offre formulée comme un paiement peut parfois passer, et une formulation inhabituelle peut attendre dans la Boîte de réception au lieu d'être ajoutée. Limitez chaque raccourci à l'expéditeur ou à l'objet de votre banque, pour que des messages sans rapport ne soient jamais envoyés à Damla.

## À voir aussi

- [L'assistant de configuration des automatisations](/guide/capture/setup-wizard/)
- [La boîte de réception](/guide/recording/the-inbox/)
- [Ce que Damla ignore, et annuler une alerte](/guide/capture/what-damla-ignores/)
- [Importer un relevé](/guide/capture/importing-statements/)

![Réglages > Messages et relevés de la banque > Automatisations.](damla-automations.png)
