# Data on the 10 most recent presidents.  Data sources:
# http://us-presidents.insidegov.com/
# https://data.bls.gov/timeseries/LNS14000000
# http://www.gallup.com/poll/116677/presidential-approval-ratings-gallup-historical-statistics-trends.aspx
# Education data was gathered from Wikipedia
USPresidentsData = {
    "Donald Trump": {
        "Term Start": 2017,
        "Term End": None,
        "Party": "Republican",
        "Vice President": ["Mike Pence"],
        "Birth": {
            "Location": "New York, NY",
            "Date": "June 14",
            "Year": 1946,
        },
        "Spouse": "Melania Trump",
        "Unemployment Rate": None,  # In last month of presidency
        "Approval Rating": None,  # Average approval percent
        "Education": ["Fordham University", "University of Pennsylvania"],
    },
    "Barack Obama": {
        "Term Start": 2009,
        "Term End": 2017,
        "Party": "Democratic",
        "Vice President": ["Joe Biden"],
        "Birth": {
            "Location": "Honolulu, HI",
            "Date": "August 4",
            "Year": 1961,
        },
        "Spouse": "Michelle Obama",
        "Unemployment Rate": 4.8,  # In last month of presidency
        "Approval Rating": 47.9,  # Average approval percent
        "Education": ["Occidental College", "Columbia University", "Harvard University"],
    },
    "George W. Bush": {
        "Term Start": 2001,
        "Term End": 2009,
        "Party": "Republican",
        "Vice President": ["Dick Cheney"],
        "Birth": {
            "Location": "New Haven, CT",
            "Date": "July 6",
            "Year": 1946,
        },
        "Spouse": "Laura Bush",
        "Unemployment Rate": 7.8,  # In last month of presidency
        "Approval Rating": 49.4,  # Average approval percent
        "Education": ["Yale University", "Harvard University"],
    },
    "Bill Clinton": {
        "Term Start": 1993,
        "Term End": 2001,
        "Party": "Democratic",
        "Vice President": ["Al Gore"],
        "Birth": {
            "Location": "Hope, AK",
            "Date": "August 19",
            "Year": 1946,
        },
        "Spouse": "Hillary Rodham Clinton",
        "Unemployment Rate": 4.2,  # In last month of presidency
        "Approval Rating": 55.1,  # Average approval percent
        "Education": ["Georgetown University", "Oxford University", "Yale University"],
    },
    "George H. W. Bush": {
        "Term Start": 1989,
        "Term End": 1993,
        "Party": "Republican",
        "Vice President": ["Dan Quayle"],
        "Birth": {
            "Location": "Milton, MA",
            "Date": "June 12",
            "Year": 1924,
        },
        "Spouse": "Barbara Bush",
        "Unemployment Rate": 7.3,  # In last month of presidency
        "Approval Rating": 60.9,  # Average approval percent
        "Education": ["Yale University"],
    },
    "Ronald Reagan": {
        "Term Start": 1981,
        "Term End": 1989,
        "Party": "Republican",
        "Vice President": ["George H. W. Bush"],
        "Birth": {
            "Location": "Tampico, IL",
            "Date": "February 6",
            "Year": 1911,
        },
        "Spouse": "Nancy Reagan",
        "Unemployment Rate": 5.4,  # In last month of presidency
        "Approval Rating": 52.8,  # Average approval percent
        "Education": ["Eureka College"],
    },
    "Jimmy Carter": {
        "Term Start": 1977,
        "Term End": 1981,
        "Party": "Democratic",
        "Vice President": ["Walter Mondale"],
        "Birth": {
            "Location": "Plains, GA",
            "Date": "October 1",
            "Year": 1924,
        },
        "Spouse": "Eleanor Rosalynn Carter",
        "Unemployment Rate": 7.5,  # In last month of presidency
        "Approval Rating": 45.5,  # Average approval percent
        "Education": ["United States Naval Academy"],
    },
    "Gerald Ford": {
        "Term Start": 1974,
        "Term End": 1977,
        "Party": "Republican",
        "Vice President": ["Nelson Rockefeller"],
        "Birth": {
            "Location": "Omaha, NE",
            "Date": "July 14",
            "Year": 1913,
        },
        "Spouse": "Elizabeth Ann \"Betty\" Ford",
        "Unemployment Rate": 7.5,  # In last month of presidency
        "Approval Rating": 47.2,  # Average approval percent
        "Education": ["University of Michigan Ann-Arbor", "Yale University"],
    },
    "Richard Nixon": {
        "Term Start": 1969,
        "Term End": 1974,
        "Party": "Republican",
        "Vice President": ["Spiro Agnew", "Gerald Ford"],
        "Birth": {
            "Location": "Yorba Linda, CA",
            "Date": "January 9",
            "Year": 1913,
        },
        "Spouse": "Thelma Catherine \"Pat\" Nixon",
        "Unemployment Rate": 5.1,  # In last month of presidency
        "Approval Rating": 49.0,  # Average approval percent
        "Education": ["Whittier College", "Duke University"],
    },
    "Lyndon Johnson": {
        "Term Start": 1963,
        "Term End": 1969,
        "Party": "Democratic",
        "Vice President": ["Hubert Humphrey"],
        "Birth": {
            "Location": "Stonewall, TX",
            "Date": "August 27",
            "Year": 1908,
        },
        "Spouse": "Claudia Alta \"Lady Bird\" Johnson",
        "Unemployment Rate": 3.4,  # In last month of presidency
        "Approval Rating": 55.1,  # Average approval percent
        "Education": ["Texas State University"],
    },
}
