import matplotlib.pyplot as plt
import LoadandSave as read

data = read.read_json("./posts_baker_2.json")
print(data)


def plot_comments_over_time(posts):
    # Create a list of tuples with the date and the total comments for each post
    data = [(post['Created On'], post['Total Comments']) for post in posts.values()]

    # Sort the data by date
    data = sorted(data, key=lambda x: x[0])

    # Extract the dates and the comment counts into separate lists
    dates, comment_counts = zip(*data)

    # Plot the data
    fig, ax = plt.subplots()
    ax.plot(dates, comment_counts)

    # Format the x-axis labels
    ax.xaxis.set_major_locator(plt.MaxNLocator(10))
    ax.xaxis.set_visible(False)


    # Set the axis labels and title
    ax.set_xlabel('Date')
    ax.set_ylabel('Number of Comments')
    ax.set_title('Number of Comments Over Time From 8-1-2022')

    # Show the plot
    plt.show()

plot_comments_over_time(data)