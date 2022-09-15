

# Bar plot of Crop_Damage_value_counts
df.groupby(['Outcome'])['Glucose'].mean().plot(
    kind = 'bar',
    xlabel = 'Diabetes Class', 
    ylabel = 'Glucose Average count',
    title = 'Glucose level of Patient Diabetes status'
);