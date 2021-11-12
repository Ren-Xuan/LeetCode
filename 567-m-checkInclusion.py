
from collections import Counter
import collections


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m = dict()
        for e in range(26):
            m[e]=0
        #m = dict(Counter(s1))
        for e in s1:
            m[ord(e)-ord('a')]+=1
        
        dic = m.copy()
        left = 0
        right = 0
        changed = False
        while right!=len(s2):
            if dic[ord(s2[right])-ord('a')]>0:
                changed = True
                dic[ord(s2[right])-ord('a')]-=1
                
                if dic[ord(s2[right])-ord('a')] == 0:
                    if all(dic[e] == 0 for e in dic):
                        return True
                right+=1
            else:
                if changed:
                    dic = m.copy()
                    changed = False
                right=left+1
                left+=1
        return False
    def checkInclusion(self, s1: str, s2: str) -> bool:
        return any([collections.Counter(s1) == collections.Counter(s2[i: i + len(s1)]) for i in range(0, len(s2) - len(s1) + 1)])

    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1 = len(s1)
        n2 = len(s2)
        if n1 > n2:
            return False 
        slist1 =[0]*26
        slist2 =[0]*26
        for i in range(n1):
            slist1[ord(s1[i])-ord('a')] += 1
            slist2[ord(s2[i])-ord('a')] += 1
        for i in range(n1,n2):
            if slist1 == slist2:
                return True 
            slist2[ord(s2[i-n1])-ord('a')] -= 1
            slist2[ord(s2[i])-ord('a')] += 1
        return True if slist1 == slist2 else False
                


s = Solution()
print(s.checkInclusion("abce","abcddeeefffff"))
print(s.checkInclusion("cgzvjlgigiosbizrtoyxexeijhqzzgbwxnmyhmanpaagjblooflawusyjiayocqhpxkybgkkybkostijmntcaxpjrfrvirvwdvlcrnrdsceldnhihrftexsdykkzcbelecdjhnwfuvnwwyxvowugdhpxfbigotfajpitxuvvcmbiipjzctrrlyxswgcvkaklfkocmathfdsgddmtstzqedazztmutaqgyiywsufcgejubzsuwcawpxwwdnzfvkpbdjuvhkrifzdtzpssbvqetzejjpdfzxczfnfoucfkvyspmpscpljmchrsfdtfcyvhfyqiaxfqdmewxtwavbxreeogxeelvrashuelrkrmxmdxriayxfmhfmxelwbydycfornyqpuhjrbgbukotgtgbtlnqljjxktnysnayiutkxuzdimbaocjymgledptwavfhlnauiafqiaoyngspnmttcxkgzufpvfvfulclgqekmehwqmfqtcrtvkfnjifrhmrsbcixlopgxkrgwnqjdhrftrwqmnfgjhwmbbmbnuawyjliarjgafybqvcigmpiyqguiwzvthtwqjvwmgfxvfwcyxizavpwwwuoqzhjyjxnjxyzpdmajxtckzdkklipdldzobgjnhyrcexggtjbilqrnfgvmtwrvhxsuysxyuumnxaucvkuafpbegihgcsuhfqqljrxrquaqpjmsegzisqogtvxcqfhnrxedovyjgyknqlfmdlpfbcyfrdokvlzlgbsnajwgnybmutvljqwovppctbadmkmujpwnggqbrcqmjbdaodixjsozzrmgoycpfkhwomujbuxqdyjmrqbchhfpwgbigboxseknxdptgoejsgewykoszssnnwaocaodqsghprzqbtnfosgotvdwxzwhjdlqhlwgidlrdudgwkgrtzdxjlhbkdjkjxjvmkvdimdeejvsmqjkagffrfsdspstowzcablbtcbpdovfinpyatkgcrzotmtztiyqnxycsawmdpfdeubekhzktgnqabfhqkfrszwpaylarurklzrfjeruqpjhhjibojcovcbccbscgwwjkixhufvbmrbbcbjiaxhhryqgbbpbzwbbbyxukrervckfislgwunqbyzandfqlsturgrssnzneqtgbsrfugstirqholqmftjacnqapjdxzrcpqfnkiuaqeyawhobemdnkshevtkywueowgekedmjdledcddtoomnkkzgvyqbonynqlakhcxynsfoxjlkevqscltkyroiiymzcxvmvhtojspzwezdxabuxuhhrgeynczmnujzglzhgywtpbyygwvazmqbcnlbjwcyzkurnsrvuxltsymrvoonasiquqvtgcffaphsfklonlsdvrmmobdafchuyntcciugpfgkuszgwrcfkbpfztiwpcczlnjoabxvtkldmtyjlbhorvhiuvzqidypyzwxqjefdhztbgcunthxzimaszfvzzfbnydxsmnplqgtrkcbadmvbqlonrxdgxpunwptatdvgxnybmviiwdrkcplezholphdenmvywilaqfujnmbeydvovytlmzpjalkekwbljwvrmemfcthyickamqdszdglrsapjjhehbiqoxhgynfyypljxhpfjxlckfxvhetcylewtnbhvgvhbpsmftgzsrzawwcunjdarwdgsqrihyshnraiizbsavcdqmjvezehjjgaxnmffdtapkzbhimygljaimqncsrynjzvkdcenndicaxnorrcbhvkgrouchpzqxtchmqabktglnjbpxhuroxjxskfppkyzbsvkenecglzbgvkxdpkjoykcsobkjnzwhbyycvkxwdwqbfzjeoakbadlaekmqgdxbojwpvkftckuparzpeyytdowcxrupeoidlirdqseqhkpfxcvfuuyqybgosfppscdtwetliojdztckjarmlkmtpuhqfhshdwummaphq",
"vnndchsddonunovgxxlrrdtnfjidmocdrdcnousrajalpsgvxolzhujffwszxhqhojtmdluwdrzwqwqvbebztgghadtdroxujmzwmftiwamymwmpysqwffjuxtdebqoglbqobxfixdlircftggnezxyxrjzytffudihaespkhdpeqnalqohjqtypsobhrxtovxskqvtdqulgaeozlxazpubdveorkytajakzagxmhrlcvfwyuteboazjnecgrggpmmxplndhbvkhmkaozlqpgxenkchjjtaegwfcbquxlsldlbxzyfwahdpybheugrysnbjizbpgpwzwfdnriscqlrndkvibkqczjbiwkahypuujuexwtbtiqpnixwcslojlowxxjhpxvmxssciyhxpbmfpoeiizuhlkswctwkzguwyvyqvtemnerodalfuocyaduvyjwcgyxtcdhggskcdazjsqnowkkklmnocgrjpgrwdwjbhvvwtgfuialbafnycigyhnphhvnibinvadcoprwdnreuwukosnlatsymuqxtgdvsrvmercfpfaaeszkhknurpqxhyyxclzvzjqkztoqrpszcmhbcdvxwbdokmflzcsepejdemzvtzhtkmhhjhducxxijvgjidjaemzwkeyggircxivxyxcogasotyfnuamfavpkcjbnvxddhyiiybwkqobmzuzmegdiqvzjptiwhujpndvxzlaclqsemhtqwufeonsdjgnbkkjjsyxtpdytfsgpmknjibjyxctwmprbcyjhlfiyaofvjryiicpoaxeonayvztnkvzpoprnbdtwllozlqyedvnezxxxuspenwxjekkgaeajhxriahqcutakhifqkzgcjldlkbxapqrwvwshpyvnbukblgcdyyhikloslaxrsfrkwexzbrndopgnwejltpdiiwykwfymmwtsbjcvtmnakjyeqcbcbdtcuxuueaxzurixojxqdfcsdmfejajqlissfkkowchuyabccuazveqmegrtdnsoqsqxgmilxnyewpkiheajdvcnyjuuuvhonjumnshoinriazaxrqizrkuhyadjmkwdizkuamgseqibgnhgovccxmgtcywroxctticxbmvvqenvmuzdobfcxqffzgcojdhvvvkgajmuelevryxxjcvfbgpztrpzjpmttwjalllbltzmfqiwoodlvnnoviwiotmpjkjwfdnjfcsylhtioszxytvkkhrunwqxuivzukynbrdjryxkivngsecgskxhtpffrvfpwrpcythjbjdjocxcaemznunyhhrvcchmubozsqnfbgwrtzhhaprjkiwwrxzggkamvzdeidbckwyctuspdmfjhhrujobvvzuhhimutzlqfleimwechdemrztldrqwtevkbmttsdxcpmkzogegytvtrwevzbvszsxpohqqndstnstnaltilpeqdixpokcgzvjlgigiosbizrtoyxexeijkqzzgbwxnmyhmanpmagjblooflawusyjiayocqhpxkpbgkkybkostijmntcaxpjrfrvirvwdvlcrnrdsceldnhihrfyexsdykkzcbelecdjhnqcuvnwwyxvowugdhpxfbigotfajpitxuvvcmbiipjzctrrlyxswgcvkahlfkocmathfdsgddmtstzqedazztmutaqgyitwsufcgejufzsuwcawpxwwdnzfvkpbdjuvhkrifzdtzpssbvqetzejjpdfzxczfnfoucfkvyspmpscpljmchrsfdqfcyvhfyqiaxfqdmewxtwavbxreeogxeelvrashuelrkrmxmdxriayxfmhfmxelwbydycfornyqpuhjrbgbukotgtgbtlnqljjxktnysnayiutkxuzdimbsocjyagledptwavfhlnauiafqiaoyngspnmttcxkgzubpvfvfulclgqekmehwqmfqtcrtxkfnjifrhmrsbcixlougxkrgwnqjdhrftrwqmnfgjhwmbbmbnuawyjliarjgafylqvcigmpiyqguiwzvthtwqjvwmgfxvfwcyvizavpwwwuoqzhjyjxnjxyzpdmajxtckzdkklipdldzobgjnhyrcexggtjbilqrnfgvmtwrvhxsuysxyuumnxaucvkuafpbegihgcsuhfqqljrxrquaqpjmsegzisqogtvxcqfhnrxedovyjgykntlfmdlpfbcyfrdokvlzlgbsnajwgnybmutvljqwovppctbadmkmujpwnggqbrcqmjbdaodixjsozzrmgoyfpfkhwomajbuxqdyjmrqbchhfpwgbigboxseknxdptgoejsgewykoszssnywaocaodqsghprzqbtnfosgotvdwxuwhjdlqhlwgidbrdudgwkgrtzdxjlhbkdjkjxjvmkvdimdeejvsmqjkagffrfsdspstowzcablbtcbpdovfinpyutkgcrzotmtztiyqnxycsawmdpfdezbekhzktgnqabfhqkfrszwpaylarurklzrfjeruqpjhhjibojcovcbccbscgwwjkixhpfvbmrbbcbjiaxhhryqgbbpbzwbbbyxukrervckfislgwunqbyzandfqlsturgrssnzneqtgbsrfugstirqholqmftjacnqapjdxzrcpqfnkiuaqeyawhobemdnkshevtkywueowgekedmjdledcddtoomnkkzgvnqbonynqlakkcxynsfoxjlkevqsyltkyroiiymzcxvmvhtojspzwezdxabuxuhhrgecnczmnujzglzhgywtpbyygwvazmqbcnlbjwcyzkurnsrvuxltsymrvoonasiquqvtgcffaphsfklonlsdvrmmobdafchuyntcciugpfgkuszgwrcfkbpfztiwpcczlnjoabxvtkldmtyjlbhorvhiuvzqidypyzwxqjefdhztbgcunthxzimaszfvzzfbnydxsmnplqgtrkcbadmvbqlonrxdgxpunwptatdvgxnybmviiwdrkcplezholphdenmvywilaqfujnmbeydvovytlmzpjalkekwbljwvrmemfcthyickamqdszdglrsapjjhehbiqoxhgynfyypljxhpfjxlckfxvhetcylewtnbhvgvhbpsmftgzsrzawwcunjdarwdgaqrihyshnraiizbsavcdqmjvezehjjgaxnmrfdtapkzbhimygljaimqncsrynjzvkdcenndicaxnorrcbhvkgrouchpzqxtchmqabktglnjbpxhuroxjxskfppkyzbsvkenecglzbgvkxdykjoykcsobkjnzwhbyycvkxwdwqbfzjeoakbadlaehmwgdxbojwpvkftckuparzpeyytdowcxrupeoidlirdqseqhkpfxcvfuuyqybgosfppscdtwetliojdztckjafmlkmtpuhqfhshdwummaphqccfbvtdzgqhgxefzzpggjsilrfchvpzmkmmdxncnqiauqkpxldmynhhqceijcmucekiqtojnotkaqrjpdhxdpxhtabmxnszocainqyzuciyktazyksdvrcerptpjrbkszgehypijcqmvpezufyhscxgowkuhexfikfqdkxemkkowkfofxskwyumvmfvpparszcldalecfmkltqmxubmbmbnanciofqaxxz"))