# Atmos #

Alfred workflow to query a python port of Matlab's [atmosisa][atm].

Retrieves temperature, speed of sound, pressure, and density at queried altitude. I mostly created this for one particular semester in
school where I had to get atmospheric values at certain altitudes. May or may not be useful to you.

## Usage ##

- `atmos <query>` — Show values for altitude <query>. Defaults to meters, but if query ends in `f` or `ft`, the proper conversion is made.
    - `↩` or `⌘+<NUM>` — Copy result to clipboard



## Licencing, thanks ##

This workflow is released under the [MIT licence][mit].
This workflow uses the [Alfred-Workflow][aw] library, which is also released under the [MIT licence][mit].


## Changelog ##

### 1.0.1 ###

- First release


[mit]: ./src/LICENCE.txt
[aw]: http://www.deanishe.net/alfred-workflow/
[atm]: http://www.mathworks.com/help/aerotbx/ug/atmosisa.html