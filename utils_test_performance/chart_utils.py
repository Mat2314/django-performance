import matplotlib.pyplot as plt


def draw_column_chart(labels: tuple, values: tuple):
    fig = plt.figure(figsize=(10, 5))

    # creating the bar plot
    plt.bar(labels, values, color='blue',
            width=0.4)

    plt.xlabel("Endpoints")
    plt.ylabel("Time of execution [seconds]")
    plt.show()
