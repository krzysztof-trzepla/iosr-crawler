import os


class SearchEngine():
    # TODO call to DB (?)
    requestedPhrases = eval(open(os.path.join(os.path.dirname(__file__), "tmp_db.phrases")).read())

    def __init__(self):
        pass

    def __str__(self):
        return str(self.requestedPhrases)

    def get_phrases(self):
        return self.requestedPhrases

    def add_phrase(self, phraseToSearch):
        self.requestedPhrases.append(phraseToSearch.lower())

    def delete_phrase(self, phraseToDelete):
        if phraseToDelete in self.requestedPhrases:
            self.requestedPhrases.remove(phraseToDelete)

    def refresh_phrases_list(self):
        # TODO call to db (?)
        self.requestedPhrases = eval(open(os.path.join(os.path.dirname(__file__), "tmp_db.phrases")).read())

    def save_phrases_list_to_db(self):
        # TODO call to db
        file = open(os.path.join(os.path.dirname(__file__), "tmp_db.phrases"),"w+")
        file.write(str(self.requestedPhrases))
        file.flush()
        file.close()

    def search_in_url(self, url, text):
        results = self.search(text)
        print {"url": url, "results": results}
        return {"url": url, "results": results}

    def search(self, toSearch):
        #TODO efektywniejsze i nie takie naiwne szukanie
        results = []
        toSearch = toSearch.lower()
        for searchedPhrase in self.requestedPhrases:
            if searchedPhrase in toSearch:
                results.append(searchedPhrase)
        return results


se = SearchEngine()
print se.get_phrases()
se.add_phrase("zupa")
se.save_phrases_list_to_db()
se.refresh_phrases_list()
print se.get_phrases()
print se.search("lorem ipsum python world war zupa")

