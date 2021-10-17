// *** WARNING: this file was generated by Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.ChartCertManager.Inputs
{

    public sealed class CertManagerServiceAccountArgs : Pulumi.ResourceArgs
    {
        [Input("annotations")]
        private InputMap<string>? _annotations;

        /// <summary>
        /// Optional additional annotations to add to the controller's ServiceAccount.
        /// </summary>
        public InputMap<string> Annotations
        {
            get => _annotations ?? (_annotations = new InputMap<string>());
            set => _annotations = value;
        }

        /// <summary>
        /// Automount API credentials for a Service Account.
        /// </summary>
        [Input("automountServiceAccountToken")]
        public Input<bool>? AutomountServiceAccountToken { get; set; }

        /// <summary>
        /// Specifies whether a service account should be created
        /// </summary>
        [Input("create")]
        public Input<bool>? Create { get; set; }

        /// <summary>
        /// The name of the service account to use. If not set and create is true, a name is generated using the fullname template.
        /// </summary>
        [Input("name")]
        public Input<string>? Name { get; set; }

        public CertManagerServiceAccountArgs()
        {
        }
    }
}
