#FROM mcr.microsoft.com/devcontainers/miniconda:0-3
#FROM ghcr.io/devcontainers/templates/miniconda:2.0.2
FROM jupyter/minimal-notebook:2023-10-17

# Set version
#ENV GDS_ENV_VERSION "1.0"

# https://github.com/ContinuumIO/docker-images/blob/master/miniconda3/Dockerfile
ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

#--- Python ---#

ADD ./gmgi221.yml /home/${NB_USER}/
RUN mamba env create -f gmgi221.yml \
 && source activate gmgi221 \
 && python -m ipykernel install --user --name gmgi221 --display-name "gmgi221" \
 && conda deactivate \
 && rm ./gmgi221.yml \
 && conda clean --all --yes --force-pkgs-dirs \
 && find /opt/conda/ -follow -type f -name '*.a' -delete \
 && find /opt/conda/ -follow -type f -name '*.pyc' -delete \
 && find /opt/conda/ -follow -type f -name '*.js.map' -delete \
 && find /opt/conda/envs/gmgi221//lib/python*/site-packages/bokeh/server/static \
    -follow -type f -name '*.js' ! -name '*.min.js' -delete \
 && pip cache purge \
 && rm -rf /home/$NB_USER/.cache/pip

# pip libraries
#ADD ./gds_py_pip.txt ./
#RUN source activate gds \
# && pip install -r gds_py_pip.txt \
# && pip cache purge \
# && rm -rf /home/$NB_USER/.cache/pip \
# && rm ./gds_py_pip.txt

# Make GDS default
RUN jupyter lab --generate-config \
 && echo "c.MultiKernelManager.default_kernel_name='gmgi221'" >> \
 /home/${NB_USER}/.jupyter/jupyter_lab_config.py \
 && echo "conda activate gmgi221" >> /home/${NB_USER}/.bashrc \
 && echo "c.KernelSpecManager.ensure_native_kernel = False" >> \
 /home/${NB_USER}/.jupyter/jupyter_lab_config.py \
# https://github.com/jupyter/notebook/issues/3674#issuecomment-397212982
 && echo "c.KernelSpecManager.whitelist = {'gmgi221'}" >> \
 /home/${NB_USER}/.jupyter/jupyter_lab_config.py
RUN jupyter kernelspec remove -y python3 
ENV PATH="/opt/conda/envs/gmgi221/bin/:${PATH}"

#--- Jupyter config ---#
USER root
# Turn off notifications
RUN jupyter labextension disable "@jupyterlab/apputils-extension:announcements" \
# Clean cache up
 && jupyter lab clean -y \
 && conda clean --all -f -y \
 && npm cache clean --force \
 && rm -rf $CONDA_DIR/share/jupyter/lab/staging \
 && rm -rf "/home/${NB_USER}/.node-gyp" \
 && rm -rf /home/$NB_USER/.cache/yarn \
# Fix permissions
 && fix-permissions "${CONDA_DIR}" \
 && fix-permissions "/home/${NB_USER}"
# Build mpl font cache
# https://github.com/jupyter/docker-stacks/blob/c3d5df67c8b158b0aded401a647ea97ada1dd085/scipy-notebook/Dockerfile#L59
USER $NB_UID
ENV XDG_CACHE_HOME="/home/${NB_USER}/.cache/"
RUN source activate gmgi221 \
 && MPLBACKEND=Agg python -c "import matplotlib.pyplot" && \
    fix-permissions "/home/${NB_USER}"

#--- htop ---#

USER root

RUN apt-get update \
 && apt-get install -y --no-install-recommends htop \
 && apt-get clean \
 && rm -rf /var/lib/apt/lists/*

# Switch back to user to avoid accidental container runs as root
USER $NB_UID


#### OLD ####
# Copy environment.yml (if found) to a temp location so we update the environment. Also
# copy "noop.txt" so the COPY instruction does not fail if no environment.yml exists.
#RUN conda install -n base -c conda-forge mamba
#COPY gmgi221.yml* .devcontainer/noop.txt /tmp/conda-tmp/
#RUN if [ -f "/tmp/conda-tmp/gmgi221.yml" ]; then umask 0002 && /opt/conda/bin/mamba env create -f /tmp/conda-tmp/gmgi221.yml; fi \
#    && rm -rf /tmp/conda-tmp

# [Optional] Uncomment to install a different version of Python than the default
# RUN conda install -y python=3.6 \
#     && pip install --no-cache-dir pipx \
#     && pipx reinstall-all

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>
