class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        unique = set()
        for email in emails:
            local, domain = email.split('@')
            if (local.find('+') > -1): local = local[:local.find('+')]
            local = local.replace('.', '')
            unique.add("@".join([local, domain]))
        return len(unique)
