

# Install

Install chromedriver (eg. apt install chromium-chromedriver)

Need python3 and run

    pip install -r requirements


# Credentials

create .env file in this directory (same as run.sh) with

    export GITHUB_USERNAME=<username>
    export GITHUB_PASSWORD=<password>


# Cron format

<table border="2" cellspacing="0" cellpadding="6" rules="groups" frame="hsides">


<colgroup>
<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />

<col  class="org-left" />
</colgroup>
<thead>
<tr>
<th scope="col" class="org-left">*</th>
<th scope="col" class="org-left">*</th>
<th scope="col" class="org-left">*</th>
<th scope="col" class="org-left">*</th>
<th scope="col" class="org-left">*</th>
</tr>
</thead>

<tbody>
<tr>
<td class="org-left">min</td>
<td class="org-left">hr</td>
<td class="org-left">day of month</td>
<td class="org-left">month</td>
<td class="org-left">day or week</td>
</tr>
</tbody>
</table>

eg. run every weekday at 8:55 am

> 55 8 \* \* 1-5 bash /path/to/run.sh

Run every weekday at 5:25 pm

> 25 17 \* \* 1-5 bash /path/to/run.sh


# Create

Make cron jobs with

    crontab -e

Add

> 55 8 \* \* 1-5 bash /path/to/run.sh
> 
> 25 17 \* \* 1-5 bash /path/to/run.sh

