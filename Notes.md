# Exploratory Data Analysis (EDA) Notes

## Classcial Data Analysis vs EDA

Classical techniques are generally quantitative in nature. They include ANOVA, t tests, chi-squared tests, and F tests.  EDA techniques are generally graphical. They include scatter plots, character plots, box plots, histograms, bihistograms, probability plots, residual plots, and mean plots. 

## Techniques for Testing Assumptions

### 4-Plot
Collection of plots used for testing validity of data.  It tests the 4 basic assumptions: 

    fixed location
    fixed variation
    randomness
    fixed distribution

It includes:

    run sequence plot (Y_i vs i)
        if flat, fixed location holds true
        if vertical spread and same over entire plot, fixed variation holds true
    lag plot (Y_i vs Y_i-1)
        if structureless, then randomness holds true
    histogram (counts vs subgroups of Y)
        if bell-shaped, then distribution is symmetric
    normal probability plot (ordered Y vs theoretical ordered Y)
        if linear, then distrubtion holds true

Usually all 4 plots are displayed in a single window for better viewing.

It should be noted that randomness is the most critical assumption that needs to be true.  If not all usual statistical tests will be invalid.