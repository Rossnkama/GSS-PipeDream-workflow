from pipedream.script_helpers import (steps, export)

import pickle
import requests

RANKING_FUNNEL_DATA = pickle.loads(b'\x80\x03}q\x00(X\x07\x00\x00\x00Primarkq\x01}q\x02(X\x13\x00\x00\x00brandAgeRangeTargetq\x03]q\x04(X\x05\x00\x00\x0019-24q\x05X\x05\x00\x00\x0025-34q\x06eX\x14\x00\x00\x00brandPartnershipTypeq\x07]q\x08X\x16\x00\x00\x00Discount Code Giveawayq\taX\x11\x00\x00\x00brandGenderTargetq\n]q\x0bX\x04\x00\x00\x00Bothq\x0caX\x19\x00\x00\x00brandFamilialNichesTargetq\r]q\x0e(X\x07\x00\x00\x00Singlesq\x0fX\x07\x00\x00\x00Couplesq\x10X\x0b\x00\x00\x00New Parentsq\x11eX\x18\x00\x00\x00brandIncomeBucketsTargetq\x12]q\x13(X\x08\x00\x00\x0050k-100kq\x14X\t\x00\x00\x00100k-250kq\x15eX\x19\x00\x00\x00brandIsOpenToPartnerIntlyq\x16]q\x17\x88aX\x1e\x00\x00\x00brandPsychographicNichesTargetq\x18]q\x19(X\x1f\x00\x00\x00Adventurers/Outdoor Enthusiastsq\x1aX\x13\x00\x00\x00Alternative/Hipsterq\x1bX\x1f\x00\x00\x00Health and Wellness Enthusiastsq\x1cX\n\x00\x00\x00Music Fansq\x1dX\n\x00\x00\x00Travellersq\x1eeX\x0b\x00\x00\x00brandValuesq\x1f]q (X\x0e\x00\x00\x00Sustainabilityq!X\r\x00\x00\x00Affordabilityq"eX\x0f\x00\x00\x00companyLocationq#]q$X\x02\x00\x00\x00UKq%auX\n\x00\x00\x00PopSocketsq&}q\'(h\x03]q((X\x05\x00\x00\x0014-18q)X\x05\x00\x00\x0019-24q*X\x05\x00\x00\x0025-34q+X\x05\x00\x00\x0035-44q,X\x05\x00\x00\x0045-65q-X\x03\x00\x00\x0065+q.eh\x07]q/(X/\x00\x00\x00Social Media Cross Promotion/Referral Marketingq0X\x10\x00\x00\x00Product Giveawayq1X\x0b\x00\x00\x00Co-Brandingq2X\x12\x00\x00\x00Contest/Sweepstakeq3X\x15\x00\x00\x00Content Collaborationq4eh\n]q5X\x05\x00\x00\x00Womenq6ah\r]q7(X\x07\x00\x00\x00Singlesq8X\x07\x00\x00\x00Couplesq9eh\x12]q:(X\x05\x00\x00\x000-50kq;X\x08\x00\x00\x0050k-100kq<X\t\x00\x00\x00100k-250kq=X\x05\x00\x00\x00250k+q>eh\x16]q?\x88ah\x18]q@(X\x1f\x00\x00\x00Adventurers/Outdoor EnthusiastsqAX\x13\x00\x00\x00Alternative/HipsterqBX\x16\x00\x00\x00Business ProfessionalsqCX\x0c\x00\x00\x00FashionistasqDX\x1f\x00\x00\x00Health and Wellness EnthusiastsqEX\x16\x00\x00\x00Technology EnthusiastsqFX\n\x00\x00\x00TravellersqGeh\x1f]qH(X\x0f\x00\x00\x00Gender EqualityqIX\x06\x00\x00\x00LuxuryqJeh#]qKX\x03\x00\x00\x00USAqLauX\x06\x00\x00\x00MethodqM}qN(h\x03]qO(X\x05\x00\x00\x0025-34qPX\x05\x00\x00\x0035-44qQeh\x07]qR(X/\x00\x00\x00Social Media Cross Promotion/Referral MarketingqSX\x10\x00\x00\x00Product GiveawayqTX\x16\x00\x00\x00Discount Code GiveawayqUeh\n]qVh6ah\r]qW(X\x07\x00\x00\x00SinglesqXX\x07\x00\x00\x00CouplesqYX\x0b\x00\x00\x00New ParentsqZeh\x12]q[X\x08\x00\x00\x0050k-100kq\\ah\x16]q]\x88ah\x18]q^(X\x0f\x00\x00\x00Family Orientedq_X\x1f\x00\x00\x00Health and Wellness Enthusiastsq`X\n\x00\x00\x00TravellersqaX\x11\x00\x00\x00Vegetarians/Veganqbeh\x1f]qc(X\x0b\x00\x00\x00ConvenienceqdX\x0e\x00\x00\x00SustainabilityqeX\r\x00\x00\x00affordabilityqfeh#]qghLauX\x06\x00\x00\x00Liptonqh}qi(h\x03]qjX\x05\x00\x00\x0025-34qkah\x07]qlX\x0b\x00\x00\x00Co-Brandingqmah\n]qnh\x0cah\r]qoX\x07\x00\x00\x00Couplesqpah\x12]qqX\t\x00\x00\x00100k-250kqrah\x16]qs\x88ah\x18]qtX\x1f\x00\x00\x00Health and Wellness Enthusiastsquah\x1f]qv(X\x07\x00\x00\x00QualityqwX\n\x00\x00\x00Minimalismqxeh#]qyh%auX\x06\x00\x00\x00Gerberqz}q{(h\x03]q|hkah\x07]q}(X/\x00\x00\x00Social Media Cross Promotion/Referral Marketingq~X\x10\x00\x00\x00Product Giveawayq\x7fX\x16\x00\x00\x00Discount Code Giveawayq\x80X\x0b\x00\x00\x00Co-Brandingq\x81X\x12\x00\x00\x00Contest/Sweepstakeq\x82X\x15\x00\x00\x00Content Collaborationq\x83eh\n]q\x84h6ah\r]q\x85X\x0b\x00\x00\x00New Parentsq\x86ah\x12]q\x87h\\ah\x16]q\x88\x88ah\x18]q\x89X\x0f\x00\x00\x00Family Orientedq\x8aah\x1f]q\x8b(X\x0e\x00\x00\x00Sustainabilityq\x8cX\x0b\x00\x00\x00Convenienceq\x8deh#]q\x8ehLauX\x06\x00\x00\x00Spruceq\x8f}q\x90(h\x03]q\x91(X\x05\x00\x00\x0019-24q\x92X\x05\x00\x00\x0025-34q\x93X\x05\x00\x00\x0035-44q\x94X\x05\x00\x00\x0045-65q\x95X\x03\x00\x00\x0065+q\x96eh\x07]q\x97(X/\x00\x00\x00Social Media Cross Promotion/Referral Marketingq\x98X\x10\x00\x00\x00Product Giveawayq\x99X\x16\x00\x00\x00Discount Code Giveawayq\x9aX\x12\x00\x00\x00Contest/Sweepstakeq\x9bX\x15\x00\x00\x00Content Collaborationq\x9ceh\n]q\x9dh\x0cah\r]q\x9e(X\x07\x00\x00\x00Singlesq\x9fX\x07\x00\x00\x00Couplesq\xa0X\x0b\x00\x00\x00New Parentsq\xa1eh\x12]q\xa2(X\x05\x00\x00\x000-50kq\xa3X\x08\x00\x00\x0050k-100kq\xa4X\t\x00\x00\x00100k-250kq\xa5X\x05\x00\x00\x00250k+q\xa6eh\x16]q\xa7\x88ah\x18]q\xa8(X\x1f\x00\x00\x00Adventurers/Outdoor Enthusiastsq\xa9X\x13\x00\x00\x00Alternative/Hipsterq\xaaX\x1a\x00\x00\x00Food & Cooking Enthusiastsq\xabX\x0f\x00\x00\x00Family Orientedq\xacX\x0c\x00\x00\x00Fashionistasq\xadX\x1f\x00\x00\x00Health and Wellness Enthusiastsq\xaeX\x1c\x00\x00\x00Self-Improvement Enthusiastsq\xafX\x11\x00\x00\x00Vegetarians/Veganq\xb0X\x05\x00\x00\x00Otherq\xb1eh\x1f]q\xb2(X\x0e\x00\x00\x00Sustainabilityq\xb3X\n\x00\x00\x00Minimalismq\xb4eh#]q\xb5h%auX\t\x00\x00\x00Jo Maloneq\xb6}q\xb7(h\x03]q\xb8(X\x05\x00\x00\x0025-34q\xb9X\x05\x00\x00\x0035-44q\xbaeh\x07]q\xbb(X/\x00\x00\x00Social Media Cross Promotion/Referral Marketingq\xbcX\x10\x00\x00\x00Product Giveawayq\xbdX\x16\x00\x00\x00Discount Code Giveawayq\xbeX\x0b\x00\x00\x00Co-Brandingq\xbfX\x12\x00\x00\x00Contest/Sweepstakeq\xc0X\x15\x00\x00\x00Content Collaborationq\xc1eh\n]q\xc2h\x0cah\r]q\xc3X\x07\x00\x00\x00Singlesq\xc4ah\x12]q\xc5(X\x08\x00\x00\x0050k-100kq\xc6X\t\x00\x00\x00100k-250kq\xc7eh\x16]q\xc8\x88ah\x18]q\xc9(X\x0c\x00\x00\x00Fashionistasq\xcaX\x1f\x00\x00\x00Health and Wellness Enthusiastsq\xcbX\n\x00\x00\x00Music Fansq\xcceh\x1f]q\xcd(X\x16\x00\x00\x00Support for Minoritiesq\xceX\r\x00\x00\x00Affordabilityq\xcfeh#]q\xd0h%auX\x0b\x00\x00\x00Ghirardelliq\xd1}q\xd2(h\x03]q\xd3hkah\x07]q\xd4(X\x10\x00\x00\x00Product Giveawayq\xd5X\x16\x00\x00\x00Discount Code Giveawayq\xd6X\x15\x00\x00\x00Content Collaborationq\xd7eh\n]q\xd8h\x0cah\r]q\xd9(X\x07\x00\x00\x00Singlesq\xdaX\x07\x00\x00\x00Couplesq\xdbX\x0b\x00\x00\x00New Parentsq\xdceh\x12]q\xddX\x05\x00\x00\x000-50kq\xdeah\x16]q\xdf\x88ah\x18]q\xe0X\x11\x00\x00\x00Vegetarians/Veganq\xe1ah\x1f]q\xe2(X\x06\x00\x00\x00 Veganq\xe3X\x0e\x00\x00\x00Sustainabilityq\xe4X\x06\x00\x00\x00Luxuryq\xe5eh#]q\xe6hLauX\n\x00\x00\x00HommeGirlsq\xe7}q\xe8(h\x03]q\xe9hkah\x07]q\xea(X/\x00\x00\x00Social Media Cross Promotion/Referral Marketingq\xebX\x10\x00\x00\x00Product Giveawayq\xecX\x16\x00\x00\x00Discount Code Giveawayq\xedX\x12\x00\x00\x00Contest/Sweepstakeq\xeeX\x15\x00\x00\x00Content Collaborationq\xefeh\n]q\xf0h6ah\r]q\xf1hpah\x12]q\xf2h\xdeah\x16]q\xf3\x88ah\x18]q\xf4X\x0c\x00\x00\x00Fashionistasq\xf5ah\x1f]q\xf6(X\x06\x00\x00\x00Luxuryq\xf7X\x07\x00\x00\x00Qualityq\xf8eh#]q\xf9h%auX\x0b\x00\x00\x00Magic Spoonq\xfa}q\xfb(h\x03]q\xfc(X\x03\x00\x00\x000-7q\xfdX\x04\x00\x00\x007-13q\xfeX\x05\x00\x00\x0014-18q\xffX\x05\x00\x00\x0019-24r\x00\x01\x00\x00X\x05\x00\x00\x0025-34r\x01\x01\x00\x00X\x05\x00\x00\x0035-44r\x02\x01\x00\x00X\x05\x00\x00\x0045-65r\x03\x01\x00\x00X\x03\x00\x00\x0065+r\x04\x01\x00\x00eh\x07]r\x05\x01\x00\x00(X/\x00\x00\x00Social Media Cross Promotion/Referral Marketingr\x06\x01\x00\x00X\x10\x00\x00\x00Product Giveawayr\x07\x01\x00\x00X\x16\x00\x00\x00Discount Code Giveawayr\x08\x01\x00\x00X\x0b\x00\x00\x00Co-Brandingr\t\x01\x00\x00X\x12\x00\x00\x00Contest/Sweepstaker\n\x01\x00\x00X\x15\x00\x00\x00Content Collaborationr\x0b\x01\x00\x00eh\n]r\x0c\x01\x00\x00h\x0cah\r]r\r\x01\x00\x00(X\x07\x00\x00\x00Singlesr\x0e\x01\x00\x00X\x07\x00\x00\x00Couplesr\x0f\x01\x00\x00X\x0b\x00\x00\x00New Parentsr\x10\x01\x00\x00eh\x12]r\x11\x01\x00\x00(X\x05\x00\x00\x000-50kr\x12\x01\x00\x00X\x08\x00\x00\x0050k-100kr\x13\x01\x00\x00X\t\x00\x00\x00100k-250kr\x14\x01\x00\x00X\x05\x00\x00\x00250k+r\x15\x01\x00\x00eh\x16]r\x16\x01\x00\x00\x88ah\x18]r\x17\x01\x00\x00(X\x1f\x00\x00\x00Adventurers/Outdoor Enthusiastsr\x18\x01\x00\x00X\x16\x00\x00\x00Business Professionalsr\x19\x01\x00\x00X\x1a\x00\x00\x00Food & Cooking Enthusiastsr\x1a\x01\x00\x00X\x0f\x00\x00\x00Family Orientedr\x1b\x01\x00\x00X\x1f\x00\x00\x00Health and Wellness Enthusiastsr\x1c\x01\x00\x00X\x1c\x00\x00\x00Self-Improvement Enthusiastsr\x1d\x01\x00\x00X\n\x00\x00\x00Travellersr\x1e\x01\x00\x00X\x11\x00\x00\x00Vegetarians/Veganr\x1f\x01\x00\x00eh\x1f]r \x01\x00\x00(X\x07\x00\x00\x00Qualityr!\x01\x00\x00X\x05\x00\x00\x00Veganr"\x01\x00\x00eh#]r#\x01\x00\x00hLauX\x04\x00\x00\x00TUMIr$\x01\x00\x00}r%\x01\x00\x00(h\x03]r&\x01\x00\x00hkah\x07]r\'\x01\x00\x00(X\x10\x00\x00\x00Product Giveawayr(\x01\x00\x00X\x0b\x00\x00\x00Co-Brandingr)\x01\x00\x00eh\n]r*\x01\x00\x00X\x03\x00\x00\x00Menr+\x01\x00\x00ah\r]r,\x01\x00\x00(X\x07\x00\x00\x00Singlesr-\x01\x00\x00X\x07\x00\x00\x00Couplesr.\x01\x00\x00eh\x12]r/\x01\x00\x00h\\ah\x16]r0\x01\x00\x00\x88ah\x18]r1\x01\x00\x00X\x16\x00\x00\x00Business Professionalsr2\x01\x00\x00ah\x1f]r3\x01\x00\x00(X\x0f\x00\x00\x00Gender Equalityr4\x01\x00\x00X\r\x00\x00\x00Affordabilityr5\x01\x00\x00eh#]r6\x01\x00\x00hLauX\x06\x00\x00\x00Olipopr7\x01\x00\x00}r8\x01\x00\x00(h\x03]r9\x01\x00\x00(X\x05\x00\x00\x0019-24r:\x01\x00\x00X\x05\x00\x00\x0025-34r;\x01\x00\x00X\x05\x00\x00\x0035-44r<\x01\x00\x00eh\x07]r=\x01\x00\x00(X/\x00\x00\x00Social Media Cross Promotion/Referral Marketingr>\x01\x00\x00X\x16\x00\x00\x00Discount Code Giveawayr?\x01\x00\x00X\x0b\x00\x00\x00Co-Brandingr@\x01\x00\x00X\x12\x00\x00\x00Contest/SweepstakerA\x01\x00\x00X\x15\x00\x00\x00Content CollaborationrB\x01\x00\x00eh\n]rC\x01\x00\x00h6ah\r]rD\x01\x00\x00(X\x07\x00\x00\x00SinglesrE\x01\x00\x00X\x07\x00\x00\x00CouplesrF\x01\x00\x00X\x0b\x00\x00\x00New ParentsrG\x01\x00\x00eh\x12]rH\x01\x00\x00hrah\x16]rI\x01\x00\x00\x88ah\x18]rJ\x01\x00\x00(X\x13\x00\x00\x00Alternative/HipsterrK\x01\x00\x00X\x16\x00\x00\x00Business ProfessionalsrL\x01\x00\x00X\x1a\x00\x00\x00Food & Cooking EnthusiastsrM\x01\x00\x00X\x0c\x00\x00\x00FashionistasrN\x01\x00\x00X\x1f\x00\x00\x00Health and Wellness EnthusiastsrO\x01\x00\x00X\n\x00\x00\x00Music FansrP\x01\x00\x00X\x1c\x00\x00\x00Self-Improvement EnthusiastsrQ\x01\x00\x00X\x16\x00\x00\x00Technology EnthusiastsrR\x01\x00\x00X\n\x00\x00\x00TravellersrS\x01\x00\x00eh\x1f]rT\x01\x00\x00(X\x0b\x00\x00\x00ConveniencerU\x01\x00\x00X\n\x00\x00\x00MinimalismrV\x01\x00\x00eh#]rW\x01\x00\x00hLauX\x07\x00\x00\x00SavetterX\x01\x00\x00}rY\x01\x00\x00(h\x03]rZ\x01\x00\x00(X\x05\x00\x00\x0025-34r[\x01\x00\x00X\x05\x00\x00\x0035-44r\\\x01\x00\x00eh\x07]r]\x01\x00\x00(X/\x00\x00\x00Social Media Cross Promotion/Referral Marketingr^\x01\x00\x00X\x10\x00\x00\x00Product Giveawayr_\x01\x00\x00X\x16\x00\x00\x00Discount Code Giveawayr`\x01\x00\x00X\x0b\x00\x00\x00Co-Brandingra\x01\x00\x00X\x12\x00\x00\x00Contest/Sweepstakerb\x01\x00\x00X\x15\x00\x00\x00Content Collaborationrc\x01\x00\x00eh\n]rd\x01\x00\x00h6ah\r]re\x01\x00\x00h\xc4ah\x12]rf\x01\x00\x00h\\ah\x16]rg\x01\x00\x00\x88ah\x18]rh\x01\x00\x00h\xf5ah\x1f]ri\x01\x00\x00(X\x07\x00\x00\x00Qualityrj\x01\x00\x00X\x06\x00\x00\x00Luxuryrk\x01\x00\x00eh#]rl\x01\x00\x00hLauX\t\x00\x00\x00Lululemonrm\x01\x00\x00}rn\x01\x00\x00(h\x03]ro\x01\x00\x00(X\x05\x00\x00\x0025-34rp\x01\x00\x00X\x05\x00\x00\x0035-44rq\x01\x00\x00X\x05\x00\x00\x0045-65rr\x01\x00\x00eh\x07]rs\x01\x00\x00(X/\x00\x00\x00Social Media Cross Promotion/Referral Marketingrt\x01\x00\x00X\x10\x00\x00\x00Product Giveawayru\x01\x00\x00X\x16\x00\x00\x00Discount Code Giveawayrv\x01\x00\x00X\x15\x00\x00\x00Content Collaborationrw\x01\x00\x00eh\n]rx\x01\x00\x00h6ah\r]ry\x01\x00\x00hpah\x12]rz\x01\x00\x00(X\x08\x00\x00\x0050k-100kr{\x01\x00\x00X\t\x00\x00\x00100k-250kr|\x01\x00\x00eh\x16]r}\x01\x00\x00\x88ah\x18]r~\x01\x00\x00(X\x16\x00\x00\x00Business Professionalsr\x7f\x01\x00\x00X\x0c\x00\x00\x00Fashionistasr\x80\x01\x00\x00X\x1f\x00\x00\x00Health and Wellness Enthusiastsr\x81\x01\x00\x00eh\x1f]r\x82\x01\x00\x00(X\x07\x00\x00\x00Qualityr\x83\x01\x00\x00X\r\x00\x00\x00Affordabilityr\x84\x01\x00\x00eh#]r\x85\x01\x00\x00hLauX\x0c\x00\x00\x00Golden Ratior\x86\x01\x00\x00}r\x87\x01\x00\x00(h\x03]r\x88\x01\x00\x00(X\x05\x00\x00\x0019-24r\x89\x01\x00\x00X\x05\x00\x00\x0025-34r\x8a\x01\x00\x00X\x05\x00\x00\x0035-44r\x8b\x01\x00\x00X\x05\x00\x00\x0045-65r\x8c\x01\x00\x00eh\x07]r\x8d\x01\x00\x00(X/\x00\x00\x00Social Media Cross Promotion/Referral Marketingr\x8e\x01\x00\x00X\x10\x00\x00\x00Product Giveawayr\x8f\x01\x00\x00X\x16\x00\x00\x00Discount Code Giveawayr\x90\x01\x00\x00X\x0b\x00\x00\x00Co-Brandingr\x91\x01\x00\x00X\x12\x00\x00\x00Contest/Sweepstaker\x92\x01\x00\x00X\x15\x00\x00\x00Content Collaborationr\x93\x01\x00\x00eh\n]r\x94\x01\x00\x00h\x0cah\r]r\x95\x01\x00\x00(X\x07\x00\x00\x00Singlesr\x96\x01\x00\x00X\x07\x00\x00\x00Couplesr\x97\x01\x00\x00eh\x12]r\x98\x01\x00\x00(X\x05\x00\x00\x000-50kr\x99\x01\x00\x00X\x08\x00\x00\x0050k-100kr\x9a\x01\x00\x00X\t\x00\x00\x00100k-250kr\x9b\x01\x00\x00X\x05\x00\x00\x00250k+r\x9c\x01\x00\x00eh\x16]r\x9d\x01\x00\x00\x88ah\x18]r\x9e\x01\x00\x00(X\x1f\x00\x00\x00Adventurers/Outdoor Enthusiastsr\x9f\x01\x00\x00X\x16\x00\x00\x00Business Professionalsr\xa0\x01\x00\x00X\n\x00\x00\x00Music Fansr\xa1\x01\x00\x00X\x1c\x00\x00\x00Self-Improvement Enthusiastsr\xa2\x01\x00\x00X\x0b\x00\x00\x00Sports Fansr\xa3\x01\x00\x00X\n\x00\x00\x00Travellersr\xa4\x01\x00\x00eh\x1f]r\xa5\x01\x00\x00(X\x16\x00\x00\x00Support for Minoritiesr\xa6\x01\x00\x00X\r\x00\x00\x00Affordabilityr\xa7\x01\x00\x00X\x07\x00\x00\x00Qualityr\xa8\x01\x00\x00eh#]r\xa9\x01\x00\x00h%auu.')
USER_CHOICES_RESPONSE = steps["trigger"]["event"]["body"]["form_response"]["answers"]
RESPONSE_INDEX_FIELD_MAPPING = {
  "0": "emailAddress",
  "1": "brandGenderTarget",
  "2": "brandAgeRangeTarget",
  "3": "brandIncomeBucketsTarget",
  "4": "brandFamilialNichesTarget",
  "5": "brandPsychographicNichesTarget",
  "6": "brandIsOpenToPartnerIntly",
  "7": "brandValues",
  "8": "brandPartnershipType"
}

def flatten(list_to_flatten):
  return [item for sublist in list_to_flatten for item in sublist]

def extract_choices_from_response(resp):
  choices = []
  for i in range(1, 8):
    response_field = resp[i]
    if 'choice' in response_field:
      choice = [resp[i]['choice']['label']]
    elif "boolean" in response_field:
      choice = [resp[i]['boolean']]
    else:
      choice = resp[i]['choices']['labels']
    choices.append(choice)
  return choices

def rank_user_partner_by_brand_similarity_distance(user_profile):
  heuristic_pool_ranking = {}
  for brand, brand_data in RANKING_FUNNEL_DATA.items():
    buffer = []
    for i in range(1, 8):
      buffer.append(
        RANKING_FUNNEL_DATA[brand][RESPONSE_INDEX_FIELD_MAPPING[str(i)]])
    buffer = flatten(buffer)
    flat_choices = flatten(user_profile)
    flat_pool = set(flat_choices)
    heuristic_pool_ranking[brand] = len(flat_pool.difference(set(buffer)))
  return heuristic_pool_ranking

def get_best_brand_matches(brand_rankings):
  min_value = min(brand_rankings.values())
  return {key:value for key, value in brand_rankings.items() if value == min_value}

def format_best_matches(best_matches):
  s = '\n'
  for i in get_best_brand_matches(best_matches):
    s  = s + f'{i} \n'
  return s

def send_simple_message(recipient_addr, best_matches):
	return requests.post(
		"https://api.mailgun.net/v3/sandbox857de594e295492b867b832b905482dc.mailgun.org/messages",
		auth=("api", "a1665b9eb7d3826973c4519a957d2bfd-1b3a03f6-c11ac2d6"),
		data={"from": "Mailgun Sandbox <postmaster@sandbox857de594e295492b867b832b905482dc.mailgun.org>",
			"to": f"<{recipient_addr}>",
			"subject": "Get Shop Swap recommendation",
			"text": f"Congratulations we've worked out your best match(es) they're: {best_matches}"})

user_choices_profile = extract_choices_from_response(USER_CHOICES_RESPONSE)
rankings = rank_user_partner_by_brand_similarity_distance(user_choices_profile)
best_matches = get_best_brand_matches(rankings)
fbest_matches = format_best_matches(best_matches)
send_simple_message(USER_CHOICES_RESPONSE[0]['email'], fbest_matches)