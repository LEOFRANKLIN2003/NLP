#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install sumy')


# In[2]:


from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.text_rank import TextRankSummarizer


# In[3]:


text ="""
Amar, the head of a black-ops squad is summoned by Police commissioner Jose to bring justice to a group of masked vigilantes for the murder of Stephen Raj, who was killed following his arrest and subsequent release after being imprisoned for aiding Adaikalam and Anbu in the murder of ACP Prabhajaran and his foster father, Karnan.[a] Amar leads the investigation by digging into Karnan's life, as he finds the murder out of place since Karnan was an ordinary man while the other two were high-ranking NCB officials.  Amar learns of Karnan's recent addiction to alcohol, drugs and prostitutes, while concurrently being overprotective of his infant foster grandson. Whilst investigating, Amar learns of two missing shipping containers of drugs being hunted by Sandhanam, who runs a much bigger syndicate than Adaikalam, named Vetti Vagaiyara. The other two containers were supposed to have been delivered to his cold-blooded smuggler boss, Rolex. The latter had promised to help Sandhanam form his own government if the drugs were delivered; if not Sandhanam and his family would be killed. Amar slowly figures out that all of Karnan's addictions were a ruse to cover up a covert operation he had been running.  Meanwhile, Veerapandian, a PWD officer, assigns a meeting with the gangsters at a theatre, where he reveals that he along with a contractor named Rudra Prathap know the location of the containers as they want to deliver them to Rolex, bypassing Sandhanam. However, the masked vigilantes arrive and kill Veerapandian by slitting his throat. Amar and his team arrive at the scene, having learnt of the events through a tracking chip left by Karnan, and capture one of the vigilantes, Bejoy. Amar interrogates Bejoy who discloses that his family were killed for his role in leading an earlier drugs bust,[a] leaving them to join the vigilantes. Realizing that Rudra Prathap is also one of the vigilantes' next targets, Amar and his team sneak into Rudra Prathap's daughter's wedding ceremony, where Prathap has invited Sandhanam for protection, fearing for his life and family.  The masked men, along with their leader, arrive at the wedding, where the leader threatens Prathap by holding his daughter at knifepoint. The leader drags Prathap and escapes on a bike, leaving the other members to deal with Sandhanam, however he defeats them. Amar chases the leader and confronts him. The leader video calls Sandhanam and reveals himself to be Karnan, who is infact alive and had faked his own death. Karnan kills Prathap by slitting his throat and escapes from the police. Amar reveals to Jose that Karnan is actually Vikram, the former commander of the black-ops squad 1986 pilot batch. After a botched mission in 1991 which led to the squad being branded as terrorists, the government hunted and brutally killed all of the squad members and their families; only Vikram and three other members survived. Amar comes to the conclusion that Jose is Sandhanam's mole within the department and was involved in Prabhajaran's murder. It is revealed that Prabhajaran was captured by Sandhanam with Jose's help. Sandhanam had interrogated Prabhajaran about the containers and upon his refusal to divulge any information, proceeded to kill him. Jose, Veerapandian and Prathap covered up the murder by disguising it as a terrorist attack. Amar orchestrates a bomb blast at Sandhanam's house, which destroys his bungalow and a drug lab in his basement. Jose informs Sandhanam of the bombing just in time and everyone except Sandhanam's brother Elango evacuate from the blast site. Jose reveals Vikram and Amar's identities to Sandhanam.  Later, Vikram arrives at the prison, and frees Bejoy and his team. Sandhanam brutally kills Amar's wife Gayathri, by decapitating her and sends his men to attack Vikram's daughter-in-law and grandson at Prabhajaran's residence. Having already expected this, Vikram rushes to save them, where a member of Vikram's pilot black-ops squad, Tina who was posing as the servant of the house under the name of Valiamma, is killed whilst protecting Vikram's daughter-in-law and grandson. Distraught at his wife's death, Amar joins Vikram's gang to take down Sandhanam and his syndicate. He arrives at Jose's house and kills him after learning of his involvment in Gayathri's murder.  Vikram and his grandson reach Chennai Port where the hidden containers are hidden. Sandhanam learns about the location of the containers and attacks Vikram. Vikram mows down Sandhanam's men with a cannon and an M2 Browning but the remaining members of his black ops squad, Agents Uppiliappan and Lawrence, are killed in the scuffle. Vikram blows up Sandhanam's containers and Sandhanam is killed in the midst. After Gayathri's funeral in Ernakulam, Amar mourns Gayathri's death and with the syndicate destroyed, he vows to continue Vikram's mission by joining his team along with Bejoy.  One week later, Adaikalam and Anbu arrive with their men in the Sassoon Docks in Mumbai, and meet up with the gangsters affiliated with Sandhanam and oragnize a meeting with their boss, Rolex. Adaikalam and Anbu reveal Dilli's involvement in the Trichy drug ambush,[a] and Sandhanam's men reveal Vikram's and Amar's involvement in the destruction of their drug syndicate and the killing of their leader. Anbu informs Rolex that Dilli is hiding in Uttar Pradesh while Sandhanam's men inform him that Vikram's family are settled abroad, shown to be San Francisco. Rolex announces a huge sum as a reward for the execution of Amar, Dilli and Vikram's team. However, unknown to everyone else, Vikram is present at the meeting and walks away with determination after learning about the bounty placed on his team, Amar and Dilli.
"""


# In[4]:


def textrank_summarize(text, num_sentences=2):
    # Initialize TextRank summarizer
    summarizer = TextRankSummarizer()
    # Parse the text
    parser = PlaintextParser.from_string(text, Tokenizer("english"))
    # Get the summary
    summary = summarizer(parser.document, num_sentences)
    # Combine the sentences into a single string
    summarized_text = ' '.join([str(sentence) for sentence in summary])
    return summarized_text


# In[5]:


print("TextRank Summary:")
print(textrank_summarize(text))


# In[ ]:




