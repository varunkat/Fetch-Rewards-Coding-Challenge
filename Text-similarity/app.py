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

        sample1_lis1 = []
        sample1_lis2 = []
        sample2_lis1 = []
        sample2_lis2 = []

        x = box1.split('.')
        for i in x:
            if i is not str:
                sample1_lis1.append(i)

        for i in sample1_lis1:
            y = i.split()
            for j in y:
                sample1_lis2.append(j)


        dic1 = {}

        for word in sample1_lis2:
            dic1[word] = dic1.get(word, 0) + 1

        keys1_count = len(dic1.keys())



        y = box2.split('.')
        for i in y:
            if i is not str:
                sample2_lis1.append(i)

        for i in sample2_lis1:
            y = i.split()
            for j in y:
                sample2_lis2.append(j)

        dic2 = {}

        for word in sample2_lis2:
            dic2[word] = dic2.get(word, 0) + 1


        keys2_count = len(dic2.keys())


        key_max = max(keys1_count, keys2_count)

        lis_ex = []
        for k, v in dic1.items():
            for key, value in dic2.items():
                if k == key and v == value:
                    lis_ex.append(k)


        count = 0

        for i in lis_ex:
            count = count +1

        per = (count/key_max)*100

        result = None


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
    app.run(host='0.0.0.0', port=80)
