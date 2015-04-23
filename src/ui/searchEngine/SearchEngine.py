
class SearchEngine():

    def __init__(self):
         self.requestedPhrases = []

    def __str__(self):
        return str(self.requestedPhrases)

    def getRequestedPhrases(self):
        return self.requestedPhrases

    def addPhraseToSearch(self, phraseToSearch):
        self.requestedPhrases.append(phraseToSearch.lower())

    def deletePhraseToSearch(self, phraseToDelete):
        if phraseToDelete in self.requestedPhrases:
            self.requestedPhrases.remove(phraseToDelete)

    def search(self, textToSearch):
        #TODO efektywniejsze i nie takie naiwne szukanie
        results = []
        textToSearch = textToSearch.lower()
        for searchedPhrase in self.requestedPhrases:
            if searchedPhrase in textToSearch:
                results.append(searchedPhrase)
        return results