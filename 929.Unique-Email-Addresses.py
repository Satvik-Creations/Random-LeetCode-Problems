class Solution:
    def numUniqueEmails(self, emails: list[str]) -> int:

        emlist = []

        for email in emails:
            p = email.find("+")
            a = email.find("@")
            
            if p == -1:
                em = email[:a].replace(".","") + email[a:]
                emlist.append(em)
            else:
                em = email.replace(email[p:a],"")
                a = em.find("@")
                em = em[:a].replace(".","") + em[a:]
                emlist.append(em)
        

        return len(set(emlist))
