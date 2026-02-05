class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domains = {}
        for i in cpdomains:
            temp = i.split()
            cpd = temp[1].split('.')
            if len(cpd) == 3:
                d1 = ".".join(cpd)
                d2 = cpd[1]+"."+cpd[2]
                d3 = cpd[2]
                domains[d1] = domains.get(d1,0)+int(temp[0])
                domains[d2] = domains.get(d2,0)+int(temp[0])
                domains[d3] = domains.get(d3,0)+int(temp[0])
            elif len(cpd) == 2:
                d1 = ".".join(cpd)
                d3 = cpd[1]
                domains[d1] = domains.get(d1,0)+int(temp[0])
                domains[d3] = domains.get(d3,0)+int(temp[0])
            
        res = []
        for i in domains:
            res.append(str(domains[i])+" "+i)
        return res
