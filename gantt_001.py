import plotly.plotly as py
import plotly.figure_factory as ff

df = [dict(Task="Job A", Start='2019-01-01', Finish='2019-02-28'),
      dict(Task="Job B", Start='2019-03-05', Finish='2019-04-15'),
      dict(Task="Job C", Start='2019-02-20', Finish='2019-05-30')]

fig = ff.create_gantt(df)
py.iplot(fig, filename='gantt-simple-gantt-chart', world_readable=True)
