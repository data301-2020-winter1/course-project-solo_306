{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import os\n",
    "import matplotlib.pyplot as plt\n",
    "import seaborn as sns\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "hour_df = pd.read_csv(\"/Users/yuguixiaobai/course-project-solo_6007/data/raw/hour.csv\")\n",
    "df\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "metadata": {},
   "outputs": [],
   "source": [
    "sns.set_style('darkgrid')\n",
    "sns.set_context('talk')\n",
    "params = {'legend.fontsize': 'x-large',\n",
    "          'figure.figsize': (30, 10),\n",
    "          'axes.labelsize': 'x-large',\n",
    "          'axes.titlesize':'x-large',\n",
    "          'xtick.labelsize':'x-large',\n",
    "          'ytick.labelsize':'x-large'}\n",
    "\n",
    "plt.rcParams.update(params)\n",
    "\n",
    "\n",
    "\n",
    "fig,ax = plt.subplots()\n",
    "sns.pointplot(data=hour_df[['hour',\n",
    "                           'total_count',\n",
    "                           'season']],\n",
    "              x='hour',\n",
    "              y='total_count',\n",
    "              hue='season',\n",
    "              ax=ax)\n",
    "ax.set(title=\"Season hourly distribution of counts\"\n",
    "       \n",
    "       \n",
    "       fig,ax = plt.subplots()\n",
    "sns.barplot(data=hour_df[['month',\n",
    "                           'total_count']],\n",
    "              x='month',\n",
    "              y='total_count',\n",
    "              ax=ax)\n",
    "ax.set(title=\"Monthly distribution of counts\")\n",
    "       \n",
    "       fig,ax = plt.subplots()\n",
    "sns.barplot(data=hour_df[['season',\n",
    "                           'total_count']],\n",
    "              x='season',\n",
    "              y='total_count',\n",
    "              ax=ax)\n",
    "ax.set(title=\"Seasonal distribution of counts\")\n",
    "       \n",
    "       fig,ax = plt.subplots()\n",
    "sns.boxplot(data=hour_df[['total_count',\n",
    "                          'casual',\n",
    "                          'registered']],ax=ax)\n",
    "ax.set(title=\"Types of counts\")\n",
    "       \n",
    "       fig,ax = plt.subplots()\n",
    "sns.boxplot(data=hour_df[['total_count',\n",
    "                          'hour']],x='hour',y='total_count',ax=ax)\n",
    "ax.set(title=\"Checking for outliners in day hours\")\n",
    "       \n",
    "       fig,ax = plt.subplots()\n",
    "sns.boxplot(data=hour_df[['total_count',\n",
    "                          'temp']],x='temp',y='total_count',ax=ax)\n",
    "ax.set(title=\"Box Plot On Count Across Temperture\")\n"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3",
   "language": "python",
   "name": "python3"
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
   "version": "3.8.3"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 4
}
