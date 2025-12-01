{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6e431bd0-8b49-4f00-aeb8-3ee1951a3a99",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "import pandas as pd\n",
    "\n",
    "def load_csv(path=\"data/curriculum_data.csv\"):\n",
    "    df = pd.read_csv(path, dtype=str).fillna(\"\")\n",
    "    df[\"subject_norm\"] = df[\"Subject\"].str.lower()\n",
    "    df[\"grade_norm\"] = df[\"Grade\"].astype(str)\n",
    "    return df\n",
    "\n",
    "def search_curriculum(df, grade=None, subject=None, faith_pref=None, top_k=5):\n",
    "    q = df\n",
    "    if grade:\n",
    "        q = q[q[\"grade_norm\"] == str(grade)]\n",
    "    if subject:\n",
    "        q = q[q[\"subject_norm\"].str.contains(subject.lower(), na=False)]\n",
    "    if faith_pref:\n",
    "        # simple match on FaithBased column values\n",
    "        q = q[q[\"FaithBased\"].str.lower().isin([faith_pref.lower()])]\n",
    "    return q.head(top_k).to_dict(orient=\"records\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:base] *",
   "language": "python",
   "name": "conda-base-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.12.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
