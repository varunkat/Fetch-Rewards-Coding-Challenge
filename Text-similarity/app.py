from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('text-similarity.html')


@app.route('/send', methods=['POST'])
def send(sum=sum):
    if request.method == 'POST':
        box1 = request.form['box1']
        box2 = request.form['box2']

        str = ''

        sample1_lis1 = []   #initializing lists
        sample1_lis2 = []
        sample2_lis1 = []
        sample2_lis2 = []
# code block for processing first text
        x = box1.split('.') #splitting text into sentences and appending to list
        for i in x:
            if i is not str:
                sample1_lis1.append(i)

        for i in sample1_lis1: #splitting sentences into words and appending to list
            y = i.split()
            for j in y:
                sample1_lis2.append(j)


        dic1 = {} #initializing dictionary

        for word in sample1_lis2: #iterating through list which has words and counting frequency of each word and storing in dict
            dic1[word] = dic1.get(word, 0) + 1

        keys1_count = len(dic1.keys()) #counting the total keys

# code block for processing second text

        y = box2.split('.') #splitting text into sentences and appending to list
        for i in y:
            if i is not str:
                sample2_lis1.append(i)

        for i in sample2_lis1: #splitting sentences into words and appending to list
            y = i.split()
            for j in y:
                sample2_lis2.append(j)

        dic2 = {} #initializing dictionary

        for word in sample2_lis2:  #iterating through list which has words and counting frequency of each word and storing in dict
            dic2[word] = dic2.get(word, 0) + 1


        keys2_count = len(dic2.keys()) #counting the total keys


        key_max = max(keys1_count, keys2_count) #getting maximum value of both dict keys

  # code block for interating through dicts and checking the key and value
        lis_ex = []
        for k, v in dic1.items():
            for key, value in dic2.items():
                if k == key and v == value:
                    lis_ex.append(k) #appending keys that are matched to a list


        count = 0

        for i in lis_ex:  #iterating through the list and counting total keys that matched
            count = count +1

        per = (count/key_max)*100 # calculating percentage by using matched keys and max of keys in both dicts

        result = None

# Code block for defining metric to get a value between 0 - 1
        if per == 0:
            result = 0
        elif per > 0 and per <= 25:
            result = 0.3
        elif per > 25 and per <= 50:
            result = 0.6
        elif per > 50 and per <= 75:
            result = 0.8
        elif per > 75 and per < 100:
            result = 0.9
        else:
            result = 1

        sum = result

        return render_template('text-similarity.html', sum=sum)




if __name__ == ' __main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80) #running application on port 80
