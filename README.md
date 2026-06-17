# IR_Project

Completed:
- SQLite database setup
- Documents, queries and qrels loading
- BEIR Quora dataset integration
- Text preprocessing service
  * Normalization
  * Lowercasing
  * Punctuation removal
  * Stopword removal
  * Lemmatization
- Processed texts stored in database

Dataset statistics:
- Documents: 522,931
- Queries: 10,000
- Qrels: 15,675

- 📂 [BEIR Dataset](https://drive.google.com/file/d/1WmlwsN9zAIkHq94pY4NYngwx1vCdvVzG/view?usp=sharing)


حمّلوا المشروع: git clone ...

ثبّتوا المكتبات: pip install -r requirements.txt

ثبّتوا الداتا: حملوا ملف ir.db من [https://drive.google.com/file/d/1WmlwsN9zAIkHq94pY4NYngwx1vCdvVzG/view?usp=sharing] وضعوه في مجلد database/.

شغّلوا النظام: python main.py